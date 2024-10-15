from datetime import date, time, datetime, timedelta

n = int(input())

names_birthdays = {}

for _ in range(n):
    name, surname, birthday = input().split()
    birthday = datetime.strptime(birthday, '%d.%m.%Y')
    names_birthdays[birthday] = names_birthdays.get(birthday, '') + name + ' ' + surname

if n == len(names_birthdays):
    print(min(names_birthdays).strftime('%d.%m.%Y') + ' ' + names_birthdays[min(names_birthdays)])
else:
    print(min(names_birthdays).strftime('%d.%m.%Y') + ' ' + str(n - len(names_birthdays)+1))
