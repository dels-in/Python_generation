from datetime import datetime


def convert_date(dates):
    dates_to_del = []
    for i in range(len(dates)):
        try:
            dates[i] = datetime.strptime(dates[i], "%d.%m.%Y")
        except ValueError:
            date = dates[i].split("-")
            dates_to_del.append(dates[i])
            days = datetime.strptime(date[1], "%d.%m.%Y").toordinal() - datetime.strptime(date[0],
                                                                                          "%d.%m.%Y").toordinal() + 1
            for day in range(0, days):
                dates.append(datetime.fromordinal(datetime.strptime(date[0], "%d.%m.%Y").toordinal() + day))
    for date in dates_to_del:
        dates.remove(date)
    return dates


def is_available_date(booked_dates, date_for_booking):
    booked_dates = convert_date(booked_dates)
    date_for_booking = convert_date([date_for_booking])
    for date in date_for_booking:
        if date in booked_dates:
            return False
    else:
        return True

