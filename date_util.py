import math

def date_interp(date):
    #201905010000
    year = math.floor(date / 100000000)
    date -= year * 100000000
    month = math.floor(date / 1000000)
    date -= month * 1000000
    day  = math.floor(date / 10000)
    date -= day * 10000
    hour = date / 2400
    if month == 1:
        monthday = 0
    elif month == 2:
        monthday = 31
    elif month == 3:
        monthday = 59
    elif month == 4:
        monthday = 90
    elif month == 5:
        monthday = 120
    elif month == 6:
        monthday = 151
    elif month == 7:
        monthday = 181
    elif month == 8:
        monthday = 212
    elif month == 9:
        monthday = 243
    elif month == 10:
        monthday = 273
    elif month == 11:
        monthday = 304
    elif month == 12:
        monthday = 334
    
    day = 365 * year + monthday + day + hour
    return day
