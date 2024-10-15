from datetime import timedelta, datetime


def num_of_sundays(year):
    return datetime(year=year, month=12, day=31).strftime('%U')

