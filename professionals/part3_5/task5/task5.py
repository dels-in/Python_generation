from datetime import date, time, datetime, timedelta

today = datetime.strptime(input(), '%d.%m.%Y')

names_birthdays = {}

for _ in range(int(input())):
    name, surname, birthday = input().split()
    birthday = datetime.strptime(birthday, '%d.%m.%Y')
    names_birthdays[birthday] = names_birthdays.get(birthday, '') + name + ' ' + surname

seven_days_birthdays = {}
for birthday, name in names_birthdays.items():
    date_b = datetime.strptime(birthday.strftime('%d.%m'), '%d.%m')
    date_t = datetime.strptime(today.strftime('%d.%m'), '%d.%m')
    if 1 <= (date_b - date_t).days <= 7 or 1 <= (date_b + timedelta(days=365) - date_t).days <= 7:
        seven_days_birthdays[birthday] = name

if len(seven_days_birthdays) > 0:
    print(seven_days_birthdays[max(seven_days_birthdays)])
else:
    print('Дни рождения не планируются')
