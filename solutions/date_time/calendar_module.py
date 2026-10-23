import calendar


def weekday_name(month, day, year):
    return calendar.day_name[calendar.weekday(year, month, day)].upper()
