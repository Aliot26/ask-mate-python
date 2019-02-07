import time
from datetime import datetime

import data_manager


def generate_timestamp():
    return int(time.time())


def convert_timestamp(timestamp):
    date_time = datetime.fromtimestamp(int(timestamp))
    return date_time


# def get_processed_data(filename):
#     data = connection.get_all_data(filename)
#     for record in data:
#         date = record['submission_time']
#         record['submission_time'] = util.convert_timestamp(date)
#     return data


def sort_by_attributes(all_data, attribute, order):
    sort_order = None
    if order == 'desc':
        sort_order = True
    elif order == 'asc':
        sort_order = False
    sort_all_data = sorted(all_data, key=lambda k: k[attribute], reverse=sort_order)
    return sort_all_data



