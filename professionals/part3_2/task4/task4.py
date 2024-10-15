from datetime import date, time

def is_correct(day, month, year):
    try:
        dat = date(year, month, day)
        return True
    except ValueError:
        return False

