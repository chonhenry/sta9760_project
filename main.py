import sys
import os
from sodapy import Socrata
from src.records import show_records

# num_records = int(
#     sys.argv[1][sys.argv[1].find("=") + 1 :]
# )  # get the page_size arguments

# if len(sys.argv) > 2:  # get the num_pages arguments
#     num_pages = int(sys.argv[2][sys.argv[2].find("=") + 1 :])
# else:
#     num_pages = 0

# show_records(dict(os.environ)["APP_KEY"], num_records, num_pages)  # show the records


show_records("UqU0dFAYG8r9bTXqyFThLAeaq", 1, 10000)  # show the records
