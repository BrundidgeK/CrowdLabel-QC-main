"""Integration tests for tag report output as CSV"""


from src.qcc.io.csv_adapter import read_assignments
from src.qcc.reports.tag_reports.tag_report_output import write_to_csv

class TestTagReportOutput:

    def setup_method(self):
        a = 1 
        # set up
        pass


    def test():
        csv_input = "tests/data/min.csv"
        csv_output = "/tests/data/tag_report_output.csv"

        tags = read_assignments(csv_input)
        report = TagReportOutput()
        report.write_to_csv(tags, csv_output)





    