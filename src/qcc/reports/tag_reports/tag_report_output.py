"""Handles the output for the tag reports"""

import csv 
from typing import List

from qcc.reports.tagger_reports.tag_report import group_by_comment_and_characteristic, count_yes_no
from qcc.domain.tagassignment import TagAssignment

class TagReportOutput:

    def write_to_csv(
            self, 
            assignments: List[TagAssignment],
            output_path : str
                     ):
        
        """Generates a CSV file of the inputted Tag Assignments"""

        # Sorts the Tag Assignments by their comments and characteristics
        grouped_assignments = group_by_comment_and_characteristic(assignments)

        # Table headers
        headers = [
        "comment_id", 
        "characteristic_id", 
        "num_taggers_asked", 
        "num_yes", 
        "num_no"
        ]

        # Metrics will be added in the future

        # Opens path and creates the CSV file
        with open(output_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)

            # Sort for consistent output
            for key in sorted(grouped_assignments.keys()):
                comment_id, characteristic_id = key
                tag_list = grouped_assignments[key]

                num_taggers_asked = len(tag_list)
                num_yes, num_no = count_yes_no(tag_list)

                num_failed = num_taggers_asked - (num_yes + num_no)

                writer.writerow([
                    comment_id, 
                    characteristic_id, 
                    num_taggers_asked, 
                    num_yes, 
                    num_no
                ])
