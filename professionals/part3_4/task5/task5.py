from datetime import timedelta, datetime

first = datetime.strptime(input(), '%d.%m.%Y')
current = first
print(first.strftime('%d.%m.%Y'))

for i in range(1, 10):
    current += timedelta(days=i + 1)
    print(current.strftime('%d.%m.%Y'))
