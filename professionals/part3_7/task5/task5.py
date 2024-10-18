import calendar

date = input().split()
print(calendar.monthrange(int(date[0]), list(calendar.month_name).index(date[1]))[1])