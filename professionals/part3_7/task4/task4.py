import calendar

date = input().split()
print(calendar.monthrange(int(date[0]), int(date[1]))[1])