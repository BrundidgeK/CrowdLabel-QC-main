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

        
