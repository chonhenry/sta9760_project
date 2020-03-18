import sys
import os
from sodapy import Socrata
from src.records import manage_records, return_records
from datetime import datetime
from elasticsearch import Elasticsearch
from requests import get
from time import sleep


def create_and_update_index(index_name, doc_type):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
    except Exception:
        pass

    es.indices.put_mapping(index=index_name, doc_type=doc_type, body={doc_type: {}})

    return es


if __name__ == "__main__":
    num_records = int(
        sys.argv[1][sys.argv[1].find("=") + 1 :]
    )  # get the page_size arguments

    num_pages = 0
    output_file = None
    if len(sys.argv) > 2:
        for arg in sys.argv:
            if "num_pages" in arg:
                num_pages = int(arg[arg.find("=") + 1 :])
            elif "output" in arg:
                output_file = arg[arg.find("=") + 1 :]

    records = return_records(
        dict(os.environ)["APP_KEY"], num_records, num_pages
    )  # records is a list, each item in records is a dictionary

    es = create_and_update_index("parking-violations", "record")

    for rec in records:  # each rec is a dictionary
        rec["issue_date_datetime"] = datetime.strptime(
            rec["issue_date"], "%m/%d/%Y"
        ).date()

        try:
            rec["fine_amount_number"] = float(rec["fine_amount"])
        except:
            pass
        res = es.index(index="parking-violations", doc_type="record", body=rec,)

