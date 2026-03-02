"""Outputs the csv file for the tag reports"""

import csv 
from typing import List

from qcc.reports.tagger_reports.tag_report import group_by_comment_and_characteristic, count_yes_no
from qcc.domain.tagassignment import TagAssignment
from qcc.data_ingestion.mysql_config import MySQLConfig
from qcc.data_ingestion.mysql_importer import TableImporter
from src.qcc.io.db_adapter import DBAdapter
from qcc.metrics.agreement_strategy import LatestLabelPercentAgreement

class TagReportOutput:

    def db_to_csv(
        self,
        output_path : str
                     ):
        
        """Generates a CSV file from the SQL database of Tag Assignments"""

        config = MySQLConfig(host="localhost", user="root", password="password", database="expertiza_anonymization", port=3306)
        importer = TableImporter(config)
        db = DBAdapter(mysql_config=config, importer=importer)
        assignments = db.read_assignments()

        # Get informatino from databased here
        #assignmments = [] # Placeholder for the list of Tag Assignments from the database
        self.write_to_csv(assignments, output_path)


    def write_to_csv(
            self, 
            assignments: List[TagAssignment],
            output_path : str
                     ):
        
        grouped_assignments = group_by_comment_and_characteristic(assignments)
        label = LatestLabelPercentAgreement()

        headers = [
        "comment_id", 
        "characteristic_id", 
        "num_taggers_asked", 
        "num_yes", 
        "num_no",
        "num_failed",
        "cohen_kappa",
        "krippendorff_alpha"
        ]

        # Cohen's kappa + Krippendorff's alpha

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

                kappa = label.cohens_kappa(tag_list, characteristic=characteristic_id)
                alpha = label.krippendorff_alpha(tag_list, char=characteristic_id)
                
                writer.writerow([
                    comment_id, 
                    characteristic_id, 
                    num_taggers_asked, 
                    num_yes, 
                    num_no,
                    num_failed,
                    kappa,
                    alpha
                ])
