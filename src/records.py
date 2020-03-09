from src.api import get_records
from datetime import datetime
from elasticsearch import Elasticsearch
from requests import get
from time import sleep


def show_record(records):  # print the records to stdout
    for r in records:
        print(r)


def write_to(records, file):  # Write records to a file
    for r in records:
        file.write(str(r))


def manage_records(app_token: str, num_records: int, num_pages: int, output_file: str):
    if output_file != None:
        file = open(output_file, "w")
        file.close
        file = open(output_file, "a")

    if num_pages != 0:  # num_pages is given
        records = get_records(app_token, num_records, 0)
        for i in range(1, num_pages + 1):
            records = get_records(app_token, num_records, num_records * i)
            if output_file != None:
                write_to(records, file)
            else:
                show_record(records)
    else:  # num_pages is not given
        n = 1
        records = get_records(app_token, num_records, 0)
        show_record(records)
        while len(records) == num_records:
            records = get_records(app_token, num_records, num_records * n)
            if output_file != None:
                write_to(records, file)
            else:
                show_record(records)
            n += 1

