#!/usr/bin/env python3
"""Independent AionUi consumer for the synthetic publication-withdrawal corpus."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class FixtureContractError(ValueError):
    pass


def _object_without_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise FixtureContractError(f"duplicate JSON key {key!r}")
        value[key] = item
    return value


def _reject_number(token: str) -> None:
    raise FixtureContractError(f"non-finite number {token!r}")


def read_document(path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    if len(data) > 256_000:
        raise FixtureContractError("fixture corpus is too large")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise FixtureContractError("fixture corpus is not UTF-8") from exc
    try:
        document = json.loads(
            text,
            object_pairs_hook=_object_without_duplicates,
            parse_constant=_reject_number,
        )
    except (json.JSONDecodeError, FixtureContractError) as exc:
        raise FixtureContractError(f"invalid fixture JSON: {exc}") from exc
    if not isinstance(document, dict):
        raise FixtureContractError("fixture root must be an object")
    return document


@dataclass(frozen=True)
class Decision:
    disposition: str
    reason: str


def _require_exact(mapping: dict[str, Any], keys: tuple[str, ...], where: str) -> None:
    actual = tuple(sorted(mapping))
    expected = tuple(sorted(keys))
    if actual != expected:
        raise FixtureContractError(f"{where} field set differs: {actual!r} != {expected!r}")


def _string(value: Any, where: str, options: set[str] | None = None) -> str:
    if not isinstance(value, str) or value == "":
        raise FixtureContractError(f"{where} must be a non-empty string")
    if options is not None and value not in options:
        raise FixtureContractError(f"{where} is unsupported: {value!r}")
    return value


def _boolean(value: Any, where: str) -> bool:
    if type(value) is not bool:
        raise FixtureContractError(f"{where} must be boolean")
    return value


def decide(fixture: dict[str, Any]) -> Decision:
    consumers = fixture["consumers"]
    if not all(consumer["reachable"] for consumer in consumers):
        return Decision("blocked", "unreachable-consumer")
    if fixture["rollback"]["reintroduces_withdrawn_claim"]:
        return Decision("blocked", "rollback-reintroduces-withdrawn-claim")

    withdrawal = fixture["withdrawal"]
    if withdrawal["requested"]:
        ids = {consumer["id"] for consumer in consumers}
        completed = set(withdrawal["completed_consumers"])
        states_are_withdrawn = all(consumer["state"] == "withdrawn" for consumer in consumers)
        if completed == ids and states_are_withdrawn:
            return Decision("withdrawn", "withdrawal-complete")
        return Decision("blocked", "partial-withdrawal")

    if fixture["surface_generation"] == "stale" or any(
        consumer["state"] == "stale" for consumer in consumers
    ):
        return Decision("blocked", "stale-publication-surface")
    if fixture["evidence_status"] == "expired":
        return Decision("blocked", "expired-evidence")

    accessibility = fixture["accessibility"]
    if accessibility["diagram_present"] and not accessibility["text_alternative"]:
        return Decision("blocked", "missing-accessible-alternative")
    if fixture["privacy_review"] == "rejected":
        return Decision("blocked", "privacy-review-rejected")
    if fixture["licensing_review"] == "rejected":
        return Decision("blocked", "licensing-review-rejected")
    return Decision("publishable", "all-publication-gates-current")


def audit(document: dict[str, Any]) -> dict[str, Any]:
    _require_exact(
        document,
        (
            "schema_version",
            "corpus_id",
            "synthetic_only",
            "prohibited_material",
            "fixtures",
        ),
        "root",
    )
    if document["schema_version"] != "qso-publication-withdrawal-corpus-v1":
        raise FixtureContractError("schema version mismatch")
    if document["corpus_id"] != "synthetic-publication-withdrawal-v1":
        raise FixtureContractError("corpus id mismatch")
    if document["synthetic_only"] is not True:
        raise FixtureContractError("AionUi accepts only synthetic fixtures")

    prohibited = document["prohibited_material"]
    if (
        not isinstance(prohibited, list)
        or not prohibited
        or any(not isinstance(item, str) or item == "" for item in prohibited)
        or len(prohibited) != len(set(prohibited))
    ):
        raise FixtureContractError("prohibited_material must be a unique non-empty string list")

    fixtures = document["fixtures"]
    if not isinstance(fixtures, list) or len(fixtures) != 10:
        raise FixtureContractError("exactly 10 fixture cases are required")

    required_ids = {
        "current-publication",
        "stale-surface",
        "expired-evidence",
        "partial-withdrawal",
        "unreachable-consumer",
        "inaccessible-diagram",
        "privacy-rejection",
        "licensing-rejection",
        "rollback-reintroduces-withdrawn-claim",
        "complete-withdrawal",
    }
    ids: set[str] = set()
    claims: set[str] = set()
    report_cases: list[dict[str, str]] = []

    for fixture_number, fixture in enumerate(fixtures):
        where = f"fixture[{fixture_number}]"
        if not isinstance(fixture, dict):
            raise FixtureContractError(f"{where} must be an object")
        _require_exact(
            fixture,
            (
                "id",
                "claim_id",
                "surface_generation",
                "evidence_status",
                "consumers",
                "accessibility",
                "privacy_review",
                "licensing_review",
                "withdrawal",
                "rollback",
                "expected",
            ),
            where,
        )
        fixture_id = _string(fixture["id"], f"{where}.id")
        claim_id = _string(fixture["claim_id"], f"{where}.claim_id")
        if fixture_id in ids or claim_id in claims:
            raise FixtureContractError(f"{where} duplicates a fixture or claim identity")
        ids.add(fixture_id)
        claims.add(claim_id)

        _string(fixture["surface_generation"], f"{where}.surface_generation", {"current", "stale"})
        _string(fixture["evidence_status"], f"{where}.evidence_status", {"current", "expired"})
        _string(fixture["privacy_review"], f"{where}.privacy_review", {"approved", "rejected"})
        _string(fixture["licensing_review"], f"{where}.licensing_review", {"approved", "rejected"})

        consumers = fixture["consumers"]
        if not isinstance(consumers, list) or not consumers:
            raise FixtureContractError(f"{where}.consumers must not be empty")
        consumer_ids: set[str] = set()
        for consumer_number, consumer in enumerate(consumers):
            consumer_where = f"{where}.consumers[{consumer_number}]"
            if not isinstance(consumer, dict):
                raise FixtureContractError(f"{consumer_where} must be an object")
            _require_exact(consumer, ("id", "reachable", "state"), consumer_where)
            consumer_id = _string(consumer["id"], f"{consumer_where}.id")
            if consumer_id in consumer_ids:
                raise FixtureContractError(f"{consumer_where} repeats consumer {consumer_id!r}")
            consumer_ids.add(consumer_id)
            _boolean(consumer["reachable"], f"{consumer_where}.reachable")
            _string(
                consumer["state"],
                f"{consumer_where}.state",
                {"current", "stale", "withdrawn", "unknown"},
            )

        accessibility = fixture["accessibility"]
        if not isinstance(accessibility, dict):
            raise FixtureContractError(f"{where}.accessibility must be an object")
        _require_exact(accessibility, ("diagram_present", "text_alternative"), f"{where}.accessibility")
        _boolean(accessibility["diagram_present"], f"{where}.accessibility.diagram_present")
        _boolean(accessibility["text_alternative"], f"{where}.accessibility.text_alternative")

        withdrawal = fixture["withdrawal"]
        if not isinstance(withdrawal, dict):
            raise FixtureContractError(f"{where}.withdrawal must be an object")
        _require_exact(withdrawal, ("requested", "completed_consumers"), f"{where}.withdrawal")
        _boolean(withdrawal["requested"], f"{where}.withdrawal.requested")
        completed = withdrawal["completed_consumers"]
        if (
            not isinstance(completed, list)
            or any(not isinstance(item, str) for item in completed)
            or len(completed) != len(set(completed))
            or not set(completed).issubset(consumer_ids)
        ):
            raise FixtureContractError(f"{where}.withdrawal completion set is invalid")

        rollback = fixture["rollback"]
        if not isinstance(rollback, dict):
            raise FixtureContractError(f"{where}.rollback must be an object")
        _require_exact(rollback, ("attempted", "reintroduces_withdrawn_claim"), f"{where}.rollback")
        attempted = _boolean(rollback["attempted"], f"{where}.rollback.attempted")
        reintroduces = _boolean(
            rollback["reintroduces_withdrawn_claim"],
            f"{where}.rollback.reintroduces_withdrawn_claim",
        )
        if reintroduces and not attempted:
            raise FixtureContractError(f"{where} claims rollback reintroduction without rollback")

        expected = fixture["expected"]
        if not isinstance(expected, dict):
            raise FixtureContractError(f"{where}.expected must be an object")
        _require_exact(expected, ("disposition", "reason"), f"{where}.expected")
        expected_decision = Decision(
            _string(
                expected["disposition"],
                f"{where}.expected.disposition",
                {"publishable", "withdrawn", "blocked"},
            ),
            _string(expected["reason"], f"{where}.expected.reason"),
        )
        actual = decide(fixture)
        if actual != expected_decision:
            raise FixtureContractError(
                f"{fixture_id} expected {expected_decision} but AionUi evaluated {actual}"
            )
        report_cases.append(
            {
                "fixture_id": fixture_id,
                "disposition": actual.disposition,
                "reason": actual.reason,
            }
        )

    if ids != required_ids:
        raise FixtureContractError(
            f"fixture class coverage mismatch: missing={sorted(required_ids - ids)}, "
            f"extra={sorted(ids - required_ids)}"
        )

    return {
        "consumer": "AionUi-validation-only",
        "schema_version": document["schema_version"],
        "corpus_id": document["corpus_id"],
        "fixture_count": len(fixtures),
        "cases": report_cases,
        "authority_effect": "none",
        "publication_effect": "none",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--corpus",
        type=Path,
        default=Path("fixtures/publication-withdrawal-v1.json"),
    )
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    try:
        report = audit(read_document(args.corpus))
    except (OSError, FixtureContractError) as exc:
        print(f"AionUi publication-withdrawal audit: FAIL: {exc}")
        return 1
    output = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(output, encoding="utf-8")
    print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
