
import time

def curtime():
    # Year, Month, Day, Hour, Min, Sec, Weekday, Yearday
    return list(time.localtime())[:-1]

