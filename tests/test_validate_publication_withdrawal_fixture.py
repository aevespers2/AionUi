from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_publication_withdrawal_fixture import (
    FixtureContractError,
    audit,
    read_document,
)


CORPUS = Path("fixtures/publication-withdrawal-v1.json")


class AionUiPublicationWithdrawalFixtureTests(unittest.TestCase):
    def _temporary(self, text: str) -> Path:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "fixture.json"
        path.write_text(text, encoding="utf-8")
        return path

    def test_shared_fixture_is_accepted(self) -> None:
        report = audit(read_document(CORPUS))
        self.assertEqual(report["consumer"], "AionUi-validation-only")
        self.assertEqual(report["fixture_count"], 10)
        self.assertEqual(report["publication_effect"], "none")

    def test_duplicate_root_key_is_rejected(self) -> None:
        text = CORPUS.read_text(encoding="utf-8").replace(
            '"corpus_id": "synthetic-publication-withdrawal-v1",',
            '"corpus_id": "synthetic-publication-withdrawal-v1",\n'
            '  "corpus_id": "synthetic-publication-withdrawal-v1",',
            1,
        )
        with self.assertRaises(FixtureContractError):
            read_document(self._temporary(text))

    def test_misclassified_case_is_rejected(self) -> None:
        document = read_document(CORPUS)
        document["fixtures"][2]["expected"]["reason"] = "all-publication-gates-current"
        with self.assertRaises(FixtureContractError):
            audit(document)

    def test_unknown_withdrawal_consumer_is_rejected(self) -> None:
        document = read_document(CORPUS)
        document["fixtures"][9]["withdrawal"]["completed_consumers"].append("external-cache")
        with self.assertRaises(FixtureContractError):
            audit(document)

    def test_non_finite_value_is_rejected(self) -> None:
        text = CORPUS.read_text(encoding="utf-8").replace(
            '"synthetic_only": true',
            '"synthetic_only": Infinity',
            1,
        )
        with self.assertRaises(FixtureContractError):
            read_document(self._temporary(text))


if __name__ == "__main__":
    unittest.main()
