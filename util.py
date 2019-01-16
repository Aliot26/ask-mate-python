import time
from datetime import datetime


def generate_timestamp():
    return int(time.time())


def convert_timestamp(timestamp):
    date_time = datetime.fromtimestamp(int(timestamp))
    return date_time




