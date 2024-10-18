import calendar
import datetime

date = datetime.datetime.strptime(input(), "%Y-%m-%d")
print(calendar.day_name[calendar.weekday(date.year, date.month, date.day)])