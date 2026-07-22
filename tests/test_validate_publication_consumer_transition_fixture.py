from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

from scripts.validate_publication_consumer_transition_fixture import (
    TransitionFixtureError,
    audit_transition_corpus,
    load_document,
)


CORPUS_PATH = Path("fixtures/publication-consumer-transition-v1.json")


class PublicationConsumerTransitionFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.document = load_document(CORPUS_PATH)

    def test_valid_corpus(self) -> None:
        report = audit_transition_corpus(copy.deepcopy(self.document))
        self.assertEqual(report["fixture_count"], 12)
        self.assertEqual(report["authority_effect"], "none")
        self.assertEqual(report["publication_effect"], "none")
        by_id = {item["fixture_id"]: item for item in report["results"]}
        self.assertEqual(
            by_id["idempotent-retry-after-ack-loss"]["disposition"],
            "publishable",
        )
        self.assertEqual(
            by_id["concurrent-correction-then-withdrawal"]["disposition"],
            "withdrawn",
        )
        self.assertEqual(
            by_id["contract-generation-migration-partial"]["reason"],
            "partial-fixture-generation-migration",
        )

    def test_duplicate_key_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"schema_version":"one","schema_version":"two"}',
                encoding="utf-8",
            )
            with self.assertRaises(TransitionFixtureError):
                load_document(path)

    def test_required_consumer_omission_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        fixture = next(
            item
            for item in document["fixtures"]
            if item["id"] == "consumer-addition-unacknowledged"
        )
        fixture["consumers"] = [
            item for item in fixture["consumers"] if item["id"] != "feed"
        ]
        with self.assertRaisesRegex(TransitionFixtureError, "omits required consumers"):
            audit_transition_corpus(document)

    def test_duplicate_consumer_identity_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        fixture = document["fixtures"][0]
        fixture["consumers"].append(copy.deepcopy(fixture["consumers"][0]))
        with self.assertRaisesRegex(TransitionFixtureError, "repeats consumer identity"):
            audit_transition_corpus(document)

    def test_backward_contract_generation_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        document["fixtures"][0]["current_contract_generation"] = 2
        document["fixtures"][0]["target_contract_generation"] = 1
        with self.assertRaisesRegex(TransitionFixtureError, "cannot move backward"):
            audit_transition_corpus(document)

    def test_non_attempted_retry_cannot_hide_payload_change(self) -> None:
        document = copy.deepcopy(self.document)
        document["fixtures"][0]["retry"]["payload_equal"] = False
        with self.assertRaisesRegex(TransitionFixtureError, "non-attempted retry"):
            audit_transition_corpus(document)

    def test_stale_ack_cannot_be_promoted(self) -> None:
        document = copy.deepcopy(self.document)
        fixture = next(
            item for item in document["fixtures"] if item["id"] == "stale-acknowledgment"
        )
        fixture["expected"] = {
            "disposition": "publishable",
            "reason": "current-consumer-set",
        }
        with self.assertRaisesRegex(TransitionFixtureError, "but AionUi evaluated"):
            audit_transition_corpus(document)

    def test_withdrawal_before_correction_requires_fresh_approval(self) -> None:
        report = audit_transition_corpus(copy.deepcopy(self.document))
        result = next(
            item
            for item in report["results"]
            if item["fixture_id"] == "withdrawal-then-correction"
        )
        self.assertEqual(result["disposition"], "blocked")
        self.assertEqual(
            result["reason"],
            "fresh-approval-required-after-withdrawal",
        )

    def test_uncontrolled_copy_remains_residual_risk(self) -> None:
        report = audit_transition_corpus(copy.deepcopy(self.document))
        result = next(
            item
            for item in report["results"]
            if item["fixture_id"] == "controlled-withdrawal-uncontrolled-copy"
        )
        self.assertEqual(result["disposition"], "withdrawn")
        self.assertEqual(
            result["reason"],
            "withdrawal-complete-residual-uncontrolled-copy",
        )


if __name__ == "__main__":
    unittest.main()
