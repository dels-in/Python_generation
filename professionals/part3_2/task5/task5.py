from datetime import date, time


def is_correct(day, month, year):
    try:
        dat = date(year, month, day)
        return True
    except ValueError:
        return False


dates = []
cur_date = input()
while cur_date != "end":
    dates.append(cur_date)
    cur_date = input()

count = 0
for d in dates:
    if is_correct(int(d.split('.')[0]), int(d.split('.')[1]), int(d.split('.')[2])):
        print('Корректная')
        count += 1
    else:
        print('Некорректная')
print(count)
