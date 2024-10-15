from datetime import date


def get_min_max(dates):
    return tuple(dates) and (min(dates), max(dates))