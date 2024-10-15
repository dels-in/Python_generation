from datetime import date


def get_date_range(start, end):
    return [date.fromordinal(d) for d in range(start.toordinal(), end.toordinal() + 1)]