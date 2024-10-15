from datetime import date, time, datetime, timedelta


def choose_plural(amount, declensions):
    if amount > 9:
        if str(amount)[-1] == "1" and str(amount)[-2] != "1":
            return f'{amount} {declensions[0]}'
        elif str(amount)[-1] in "234" and str(amount)[-2] != "1":
            return f'{amount} {declensions[1]}'
        else:
            return f'{amount} {declensions[2]}'

    else:
        if str(amount)[-1] == "1":
            return f'{amount} {declensions[0]}'
        elif str(amount)[-1] in "234":
            return f'{amount} {declensions[1]}'
        else:
            return f'{amount} {declensions[2]}'


today = datetime.strptime(input(), '%d.%m.%Y %H:%M')
time_of_start = datetime.strptime('08.11.2022 12:00', '%d.%m.%Y %H:%M')

if today >= time_of_start:
    print('Курс уже вышел!')
else:
    delta = time_of_start - today
    if delta.days > 0:
        if delta.seconds // 3600 > 0:
            print(
                f'До выхода курса осталось: {choose_plural(delta.days, ("день", "дня", "дней"))} и {choose_plural(delta.seconds // 3600, ("час", "часа", "часов"))}')
        else:
            print(f'До выхода курса осталось: {choose_plural(delta.days, ("день", "дня", "дней"))}')
    else:
        if delta.seconds // 3600 > 0:
            if delta.seconds // 60 - (delta.seconds // 3600) * 60 > 0:
                print(
                    f'До выхода курса осталось: {choose_plural(delta.seconds // 3600, ("час", "часа", "часов"))} и {choose_plural((delta.seconds // 60 - (delta.seconds // 3600) * 60), ("минута", "минуты", "минут"))}')
            else:
                print(f'До выхода курса осталось: {choose_plural(delta.seconds // 3600, ("час", "часа", "часов"))}')
        else:
            print(f'До выхода курса осталось: {choose_plural(delta.seconds // 60, ("минута", "минуты", "минут"))}')
