def find_time():
    from time import strftime, gmtime
    return strftime('%Y-%m-%d %H:%M', gmtime())