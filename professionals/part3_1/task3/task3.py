from datetime import date


def saturdays_between_two_dates(start, end):
    start, end = sorted((start, end))
    return sum(
        map(lambda x: x.weekday() == 5, [date.fromordinal(d) for d in range(start.toordinal(), end.toordinal() + 1)]))

