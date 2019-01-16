import time
import datetime


def generate_timestamp():
    return int(time.time())


def convert_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)
