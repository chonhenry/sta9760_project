from sodapy import Socrata
from datetime import datetime
from elasticsearch import Elasticsearch
from requests import get
from time import sleep


def get_records(app_token: str, num_records: int, num_pages: int):
    app_token = app_token[app_token.find("{") + 1 : -1]

    client = Socrata("data.cityofnewyork.us", app_token)
    return client.get(
        "nc67-uf89", limit=num_records, offset=num_pages
    )  # limit = number of records to request from each API call ;return 1000 records if limit not given ;return a list consists of dictionary
