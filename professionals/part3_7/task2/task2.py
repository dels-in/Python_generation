import calendar

date = input().split()
print(calendar.month(int(date[0]), list(calendar.month_abbr).index(date[1])))