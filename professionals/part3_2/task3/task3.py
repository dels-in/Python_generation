from datetime import date, time

def print_good_dates(dates):
    sorted_dates = sorted(filter(lambda x: x.year == 1992 and x.month + x.day == 29, dates))
    print(*list(map(lambda x: x.strftime("%B %d, %Y"), sorted_dates)), sep="\n")
