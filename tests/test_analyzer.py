import json
import unittest
from pathlib import Path

from src.analyzer import build_report, run


class AnalyzerTests(unittest.TestCase):
    def test_build_report_counts_records(self) -> None:
        report = build_report([
            {"schema_id": "orders", "version": 2, "fields_added": 2, "fields_removed": 0},
            {"schema_id": "orders", "version": 3, "fields_added": 1, "fields_removed": 1},
        ])
        self.assertEqual(report["record_count"], 2)

    def test_run_writes_output(self) -> None:
        output_path = Path("out/test-report.json")
        report = run(Path("data/contracts.ndjson"), output_path)
        on_disk = json.loads(output_path.read_text(encoding="utf-8"))
        self.assertEqual(report["record_count"], 4)
        self.assertIn("breaking_changes", on_disk)


if __name__ == "__main__":
    unittest.main()
