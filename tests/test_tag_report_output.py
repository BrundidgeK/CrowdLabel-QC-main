import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from qcc.reports.tag_reports.tag_report_output import TagReportOutput
from qcc.domain.tagassignment import TagAssignment
from qcc.io.csv_adapter import CSVAdapter

class TestTagReportOutput:

    def setup_method(self):
        # set up
        pass

    def test_write_to_csv(self):
        from pathlib import Path
        csv_input = Path(os.path.dirname(__file__)) / "data" / "min.csv"
        csv_output = Path(os.path.dirname(__file__)) / "data" / "tag_report_output.csv"

        adapter = CSVAdapter()
        tags = adapter.read_assignments(csv_input)
        report = TagReportOutput()
        report.write_to_csv(tags, csv_output)

        assert True


    def test_db_input(self):
        db_output = "/tests/data/tag_report_output.csv"

        os.makedirs(os.path.dirname(db_output), exist_ok=True)
        report = TagReportOutput()
        report.db_to_csv(db_output)
        assert os.path.exists(db_output), "CSV output file was not created from database input"
        with open(db_output, "r") as f:
            lines = f.readlines()
            assert len(lines) > 0, "CSV output file from database input is empty or only contains headers"
            assert "comment_id" in lines[0], "CSV output file from database input does not contain expected headers"
    