import calendar
import time
import hashlib


def get_current_time():
    return calendar.timegm(time.gmtime())


def generate_md5_by_str(string_input):
    return hashlib.md5(string_input.encode())
