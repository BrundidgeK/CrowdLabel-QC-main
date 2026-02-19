"""Outputs the csv file for the tag reports"""

import csv 
from typing import List

from reports.tagger_reports.tag_report import group_by_comment_and_characteristic, count_yes_no
from qcc.domain.tagassignment import TagAssignment

class TagReportOutput:

    def write_to_csv(
            self, 
            assignments: List[TagAssignment],
            output_path : str
                     ):
        
        grouped_assignments = group_by_comment_and_characteristic(assignments)

        headers = [
        "comment_id", 
        "characteristic_id", 
        "num_taggers_asked", 
        "num_yes", 
        "num_no"
        ]

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
