from src.api import get_records


def show_record(records):
    for r in records:
        print(r)
        print("\n")


def show_records(app_token: str, num_records: int, num_pages: int):
    if num_pages != 0:  # num_pages is given
        records = get_records(app_token, num_records, 0)
        for i in range(1, num_pages + 1):
            records = get_records(app_token, num_records, num_records * i)
            show_record(records)
    else:  # num_pages is not given
        n = 1
        records = get_records(app_token, num_records, 0)
        show_record(records)
        while len(records) == num_records:
            records = get_records(app_token, num_records, num_records * n)
            show_record(records)
            n += 1

