from src.api import get_records


def show_records(app_token: str, num_records: int, num_pages: int):
    if num_pages != None:  # num_pages is given
        for i in range(num_pages):
            if i == 0:
                records = get_records(app_token, num_records)
            else:
                records = get_records(app_token, num_records, num_records * i)

            for r in records:
                print(r)
                print("\n")
    else:  # num_pages is not given
        records = get_records(app_token, num_records, 1)
        for r in records:
            print(r)
