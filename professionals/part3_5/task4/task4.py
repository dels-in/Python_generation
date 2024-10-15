from datetime import date, time, datetime, timedelta

names_birthdays = {}

for _ in range(int(input())):
    *name, birthday = input().split()
    birthday = datetime.strptime(birthday, '%d.%m.%Y')
    names_birthdays[birthday] = names_birthdays.get(birthday, []) + [name]

max_births = max(map(lambda x: len(names_birthdays[x]), names_birthdays))

for birthday in sorted(list(filter(lambda x: len(names_birthdays[x]) == max_births, names_birthdays))):
    print(birthday.strftime('%d.%m.%Y'))
