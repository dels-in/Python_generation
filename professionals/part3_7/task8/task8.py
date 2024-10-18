import calendar, datetime


def print_free_tickets_dates(year):
    thursdays = []
    for month in range(1, 13):
        count = 0
        for day in range(1, calendar.monthrange(year, month)[1]):
            if calendar.weekday(year, month, day) == 3:
                count += 1
                if count == 3:
                    thursdays.append(datetime.date(year, month, day))
    for day in thursdays:
        print(day.strftime("%d.%m.%Y"))


print_free_tickets_dates(int(input()))
