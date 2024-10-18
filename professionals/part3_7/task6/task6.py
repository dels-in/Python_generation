import calendar, datetime


def get_days_in_month(year, month):
    month = list(calendar.month_name).index(month)
    return [datetime.date(year, month, day) for day in range(1, calendar.monthrange(year, month)[1] + 1)]
