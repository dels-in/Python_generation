import calendar, datetime


def get_all_mondays(year):
    return [datetime.date(year, month, day) for month in range(1, 13) for day in
            range(1, calendar.monthrange(year, month)[1] + 1) if calendar.weekday(year, month, day) == 0]
