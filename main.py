import sys
import os
from sodapy import Socrata
from src.records import manage_records
from datetime import datetime
from elasticsearch import Elasticsearch
from requests import get
from time import sleep

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

manage_records(
    dict(os.environ)["APP_KEY"], num_records, num_pages, output_file
)  # show the records
