#!/usr/bin/env python3
"""Independent AionUi review-surface consumer for publication transition fixtures."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class TransitionFixtureError(ValueError):
    """Raised when a fixture corpus is malformed or semantically unsafe."""


def _no_duplicate_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise TransitionFixtureError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def _reject_nonfinite(token: str) -> None:
    raise TransitionFixtureError(f"non-finite JSON number {token!r}")


def load_document(path: Path) -> dict[str, Any]:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise TransitionFixtureError(f"cannot read fixture corpus: {exc}") from exc
    if len(raw) > 256_000:
        raise TransitionFixtureError("fixture corpus exceeds the 256000-byte limit")
    try:
        document = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_no_duplicate_object,
            parse_constant=_reject_nonfinite,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, TransitionFixtureError) as exc:
        raise TransitionFixtureError(f"invalid UTF-8 JSON fixture corpus: {exc}") from exc
    if not isinstance(document, dict):
        raise TransitionFixtureError("fixture corpus root must be an object")
    return document


def _exact_fields(value: dict[str, Any], expected: set[str], where: str) -> None:
    actual = set(value)
    if actual != expected:
        raise TransitionFixtureError(
            f"{where} field set differs: missing={sorted(expected - actual)}, "
            f"extra={sorted(actual - expected)}"
        )


def _string(value: Any, where: str, allowed: set[str] | None = None) -> str:
    if not isinstance(value, str) or value == "":
        raise TransitionFixtureError(f"{where} must be a non-empty string")
    if allowed is not None and value not in allowed:
        raise TransitionFixtureError(f"{where} contains unsupported value {value!r}")
    return value


def _boolean(value: Any, where: str) -> bool:
    if type(value) is not bool:
        raise TransitionFixtureError(f"{where} must be boolean")
    return value


def _integer(value: Any, where: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise TransitionFixtureError(f"{where} must be an integer >= {minimum}")
    return value


def _optional_positive_integer(value: Any, where: str) -> int | None:
    if value is None:
        return None
    return _integer(value, where, 1)


@dataclass(frozen=True)
class ReviewDecision:
    disposition: str
    reason: str


def evaluate_transition(fixture: dict[str, Any]) -> ReviewDecision:
    required_order = fixture["required_consumers"]
    required = set(required_order)
    consumers = {consumer["id"]: consumer for consumer in fixture["consumers"]}

    for consumer_id, consumer in consumers.items():
        if consumer_id not in required and not consumer["retired"]:
            return ReviewDecision("blocked", "consumer-removal-without-retirement")

    for consumer_id in required_order:
        consumer = consumers[consumer_id]
        if consumer["retired"]:
            return ReviewDecision("blocked", "required-consumer-retired-without-registry-update")
        if not consumer["reachable"]:
            return ReviewDecision("blocked", "unreachable-controlled-consumer")
        if consumer["registry_generation"] != fixture["registry_generation"]:
            return ReviewDecision("blocked", "consumer-registry-generation-mismatch")
        if consumer["ack_status"] != "current":
            reason = {
                "missing": "missing-acknowledgment",
                "stale": "stale-acknowledgment",
                "replayed": "replayed-acknowledgment",
                "conflict": "conflicting-acknowledgment",
            }[consumer["ack_status"]]
            return ReviewDecision("blocked", reason)

    retry = fixture["retry"]
    if retry["attempted"] and (
        not retry["idempotency_key_reused"] or not retry["payload_equal"]
    ):
        return ReviewDecision("blocked", "non-idempotent-retry")

    migrating = fixture["target_contract_generation"] != fixture["current_contract_generation"]
    if migrating and any(
        consumers[consumer_id]["contract_generation"] != fixture["target_contract_generation"]
        for consumer_id in required_order
    ):
        return ReviewDecision("blocked", "partial-fixture-generation-migration")

    event = fixture["event"]
    if event["kind"] == "concurrent":
        if event["order"] == "withdrawal-before-correction":
            return ReviewDecision("blocked", "fresh-approval-required-after-withdrawal")
        if not (
            event["order"] == "correction-before-withdrawal"
            and event["withdrawal_generation"] > event["correction_generation"]
        ):
            return ReviewDecision("blocked", "invalid-concurrent-event-order")
        fully_withdrawn = all(
            consumers[consumer_id]["state"] == "withdrawn"
            and consumers[consumer_id]["claim_generation"] >= event["withdrawal_generation"]
            for consumer_id in required_order
        )
        if not fully_withdrawn:
            return ReviewDecision("blocked", "partial-withdrawal")
        return ReviewDecision("withdrawn", "withdrawal-dominates-concurrent-correction")

    if event["kind"] == "withdrawal":
        fully_withdrawn = all(
            consumers[consumer_id]["state"] == "withdrawn"
            and consumers[consumer_id]["claim_generation"] >= event["generation"]
            for consumer_id in required_order
        )
        if not fully_withdrawn:
            return ReviewDecision("blocked", "partial-withdrawal")
        if fixture["uncontrolled_copy_observed"]:
            return ReviewDecision("withdrawn", "withdrawal-complete-residual-uncontrolled-copy")
        return ReviewDecision("withdrawn", "withdrawal-complete")

    fully_current = all(
        consumers[consumer_id]["state"] == "current"
        and consumers[consumer_id]["claim_generation"] >= event["generation"]
        for consumer_id in required_order
    )
    if not fully_current:
        return ReviewDecision("blocked", "partial-propagation")
    if migrating:
        return ReviewDecision("publishable", "fixture-generation-migration-complete")
    if retry["attempted"]:
        return ReviewDecision("publishable", "idempotent-retry-accepted")
    if event["kind"] == "correction":
        return ReviewDecision("publishable", "correction-propagated")
    return ReviewDecision("publishable", "current-consumer-set")


def audit_transition_corpus(document: dict[str, Any]) -> dict[str, Any]:
    _exact_fields(
        document,
        {"schema_version", "corpus_id", "synthetic_only", "prohibited_material", "fixtures"},
        "root",
    )
    if document["schema_version"] != "qso-publication-consumer-transition-corpus-v1":
        raise TransitionFixtureError("schema version mismatch")
    if document["corpus_id"] != "synthetic-publication-consumer-transition-v1":
        raise TransitionFixtureError("corpus id mismatch")
    if document["synthetic_only"] is not True:
        raise TransitionFixtureError("AionUi accepts only synthetic fixture corpora")

    prohibited = document["prohibited_material"]
    if (
        not isinstance(prohibited, list)
        or not prohibited
        or any(not isinstance(item, str) or not item for item in prohibited)
        or len(prohibited) != len(set(prohibited))
    ):
        raise TransitionFixtureError("prohibited_material must be a unique non-empty string list")

    fixtures = document["fixtures"]
    if not isinstance(fixtures, list) or len(fixtures) != 12:
        raise TransitionFixtureError("exactly 12 transition fixtures are required")

    required_fixture_ids = {
        "current-consumer-set",
        "consumer-addition-unacknowledged",
        "consumer-removal-without-retirement",
        "concurrent-correction-then-withdrawal",
        "withdrawal-then-correction",
        "controlled-withdrawal-uncontrolled-copy",
        "idempotent-retry-after-ack-loss",
        "conflicting-retry-payload",
        "contract-generation-migration-complete",
        "contract-generation-migration-partial",
        "stale-acknowledgment",
        "replayed-acknowledgment",
    }
    fixture_ids: set[str] = set()
    claim_ids: set[str] = set()
    results: list[dict[str, str]] = []

    fixture_fields = {
        "id", "claim_id", "registry_generation", "current_contract_generation",
        "target_contract_generation", "required_consumers", "consumers", "event",
        "uncontrolled_copy_observed", "retry", "expected",
    }
    consumer_fields = {
        "id", "reachable", "retired", "registry_generation", "claim_generation",
        "contract_generation", "state", "ack_status",
    }
    event_fields = {
        "kind", "generation", "correction_generation", "withdrawal_generation", "order",
    }

    for fixture_index, fixture in enumerate(fixtures):
        where = f"fixtures[{fixture_index}]"
        if not isinstance(fixture, dict):
            raise TransitionFixtureError(f"{where} must be an object")
        _exact_fields(fixture, fixture_fields, where)

        fixture_id = _string(fixture["id"], f"{where}.id")
        claim_id = _string(fixture["claim_id"], f"{where}.claim_id")
        if fixture_id in fixture_ids or claim_id in claim_ids:
            raise TransitionFixtureError(f"{where} duplicates a fixture or claim identity")
        fixture_ids.add(fixture_id)
        claim_ids.add(claim_id)

        registry_generation = _integer(fixture["registry_generation"], f"{where}.registry_generation", 1)
        current_contract = _integer(
            fixture["current_contract_generation"], f"{where}.current_contract_generation", 1
        )
        target_contract = _integer(
            fixture["target_contract_generation"], f"{where}.target_contract_generation", 1
        )
        if target_contract < current_contract:
            raise TransitionFixtureError(f"{where} target contract generation cannot move backward")
        _boolean(fixture["uncontrolled_copy_observed"], f"{where}.uncontrolled_copy_observed")

        required = fixture["required_consumers"]
        if (
            not isinstance(required, list)
            or not required
            or any(not isinstance(item, str) or not item for item in required)
            or len(required) != len(set(required))
        ):
            raise TransitionFixtureError(
                f"{where}.required_consumers must be a unique non-empty string list"
            )

        consumers = fixture["consumers"]
        if not isinstance(consumers, list) or not consumers:
            raise TransitionFixtureError(f"{where}.consumers must be a non-empty list")
        consumer_ids: set[str] = set()
        for consumer_index, consumer in enumerate(consumers):
            consumer_where = f"{where}.consumers[{consumer_index}]"
            if not isinstance(consumer, dict):
                raise TransitionFixtureError(f"{consumer_where} must be an object")
            _exact_fields(consumer, consumer_fields, consumer_where)
            consumer_id = _string(consumer["id"], f"{consumer_where}.id")
            if consumer_id in consumer_ids:
                raise TransitionFixtureError(f"{where} repeats consumer identity {consumer_id!r}")
            consumer_ids.add(consumer_id)
            _boolean(consumer["reachable"], f"{consumer_where}.reachable")
            _boolean(consumer["retired"], f"{consumer_where}.retired")
            _integer(consumer["registry_generation"], f"{consumer_where}.registry_generation", 1)
            _integer(consumer["claim_generation"], f"{consumer_where}.claim_generation", 0)
            _integer(consumer["contract_generation"], f"{consumer_where}.contract_generation", 1)
            _string(consumer["state"], f"{consumer_where}.state", {"current", "withdrawn", "unknown"})
            _string(
                consumer["ack_status"],
                f"{consumer_where}.ack_status",
                {"current", "stale", "missing", "conflict", "replayed"},
            )
        missing_consumers = set(required) - consumer_ids
        if missing_consumers:
            raise TransitionFixtureError(f"{where} omits required consumers {sorted(missing_consumers)}")

        event = fixture["event"]
        if not isinstance(event, dict):
            raise TransitionFixtureError(f"{where}.event must be an object")
        _exact_fields(event, event_fields, f"{where}.event")
        kind = _string(
            event["kind"],
            f"{where}.event.kind",
            {"current", "correction", "withdrawal", "concurrent"},
        )
        generation = _integer(event["generation"], f"{where}.event.generation", 1)
        correction = _optional_positive_integer(
            event["correction_generation"], f"{where}.event.correction_generation"
        )
        withdrawal = _optional_positive_integer(
            event["withdrawal_generation"], f"{where}.event.withdrawal_generation"
        )
        order = _string(
            event["order"],
            f"{where}.event.order",
            {"none", "correction-before-withdrawal", "withdrawal-before-correction"},
        )
        event_shape_valid = (
            kind == "current" and correction is None and withdrawal is None and order == "none"
        ) or (
            kind == "correction" and correction == generation and withdrawal is None and order == "none"
        ) or (
            kind == "withdrawal" and withdrawal == generation and correction is None and order == "none"
        ) or (
            kind == "concurrent"
            and correction is not None
            and withdrawal is not None
            and order != "none"
            and generation == max(correction, withdrawal)
        )
        if not event_shape_valid:
            raise TransitionFixtureError(f"{where} has inconsistent event generations")

        retry = fixture["retry"]
        if not isinstance(retry, dict):
            raise TransitionFixtureError(f"{where}.retry must be an object")
        _exact_fields(
            retry,
            {"attempted", "idempotency_key_reused", "payload_equal"},
            f"{where}.retry",
        )
        attempted = _boolean(retry["attempted"], f"{where}.retry.attempted")
        idempotency_key_reused = _boolean(
            retry["idempotency_key_reused"], f"{where}.retry.idempotency_key_reused"
        )
        payload_equal = _boolean(retry["payload_equal"], f"{where}.retry.payload_equal")
        if not attempted and (not idempotency_key_reused or not payload_equal):
            raise TransitionFixtureError(
                f"{where} non-attempted retry must retain neutral true values"
            )

        expected = fixture["expected"]
        if not isinstance(expected, dict):
            raise TransitionFixtureError(f"{where}.expected must be an object")
        _exact_fields(expected, {"disposition", "reason"}, f"{where}.expected")
        expected_decision = ReviewDecision(
            _string(
                expected["disposition"],
                f"{where}.expected.disposition",
                {"publishable", "withdrawn", "blocked"},
            ),
            _string(expected["reason"], f"{where}.expected.reason"),
        )

        for consumer in consumers:
            if consumer["id"] in required and consumer["registry_generation"] > registry_generation:
                raise TransitionFixtureError(
                    f"{where} consumer registry generation exceeds fixture generation"
                )

        actual_decision = evaluate_transition(fixture)
        if actual_decision != expected_decision:
            raise TransitionFixtureError(
                f"{fixture_id} expected {expected_decision} but AionUi evaluated {actual_decision}"
            )
        results.append(
            {
                "fixture_id": fixture_id,
                "disposition": actual_decision.disposition,
                "reason": actual_decision.reason,
            }
        )

    if fixture_ids != required_fixture_ids:
        raise TransitionFixtureError(
            "fixture coverage mismatch: "
            f"missing={sorted(required_fixture_ids - fixture_ids)}, "
            f"extra={sorted(fixture_ids - required_fixture_ids)}"
        )

    return {
        "consumer": "AionUi-validation-only",
        "schema_version": document["schema_version"],
        "corpus_id": document["corpus_id"],
        "fixture_count": len(fixtures),
        "results": results,
        "authority_effect": "none",
        "publication_effect": "none",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--corpus",
        type=Path,
        default=Path("fixtures/publication-consumer-transition-v1.json"),
    )
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    try:
        report = audit_transition_corpus(load_document(args.corpus))
    except (OSError, TransitionFixtureError) as exc:
        print(f"AionUi publication-consumer transition audit: FAIL: {exc}")
        return 1

    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
