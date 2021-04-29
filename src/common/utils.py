import calendar
import time


def get_current_time():
    return calendar.timegm(time.gmtime())
