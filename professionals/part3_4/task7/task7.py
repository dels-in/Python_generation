from datetime import timedelta, datetime, date


def fill_up_missing_dates(dates):
    dates = list(map(lambda x: datetime.strptime(x, "%d.%m.%Y"), dates))
    last = max(dates).toordinal()
    first = min(dates).toordinal()
    res = []
    for i in range(first, last+1):
        res.append(date.fromordinal(i))
    return [i.strftime("%d.%m.%Y") for i in res]

