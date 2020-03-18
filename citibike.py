import sys
import os
from sodapy import Socrata
from src.records import manage_records
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

    es.indices.put_mapping(
        index=index_name,
        doc_type=doc_type,
        body={doc_type: {"properties": {"location": {"type": "geo_point"}}}},
    )

    return es


def get_bike_data():
    url = "http://feeds.citibikenyc.com/stations/stations.json"
    r = get(url)
    r.raise_for_status()
    resp = r.json()
    stations = resp["stationBeanList"]  # stations is a list type

    return stations  # returns a list


if __name__ == "__main__":
    es = create_and_update_index("citibike-index", "bike")

    i = 0

    docks = get_bike_data()
    print(len(docks))

    while False:
        i += 1

        docks = get_bike_data()

        for dock in docks:
            dock["location"] = {
                "lat": dock["latitude"],
                "lon": dock["longitude"],
            }
            dock["lastCommunicationTime"] = datetime.strptime(
                dock["lastCommunicationTime"], "%Y-%m-%d %I:%M:%S %p",
            )
            res = es.index(index="citibike-index", doc_type="bike", body=dock,)
            print(res["result"])

        print(f"done loading {i}, sleeping...")
        sleep(30)
