from datetime import date, time, datetime, timedelta

left_date = datetime.strptime(input(), '%d.%m.%Y')
right_date = datetime.strptime(input(), '%d.%m.%Y')

sum_md = lambda x: x.month + x.day

for i in range((right_date - left_date).days + 1):
    if sum_md(left_date + timedelta(days=i)) % 2 == 1:
        left_date += timedelta(days=i)
        break

for i in range(0, (right_date - left_date).days + 1, 3):
    weekday = (left_date + timedelta(days=i)).weekday()
    if weekday != 0 and weekday != 3:
        print((left_date + timedelta(days=i)).strftime('%d.%m.%Y'))
