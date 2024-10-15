from datetime import date, time, datetime, timedelta

current_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')

schedule = {0: ['9:00', '21:00'], 1: ['9:00', '21:00'], 2: ['9:00', '21:00'], 3: ['9:00', '21:00'],
            4: ['9:00', '21:00'], 5: ['10:00', '18:00'], 6: ['10:00', '18:00']}

schedule_today = schedule[current_date.weekday()]

if time(hour=int(schedule_today[0].split(':')[0]),
        minute=int(schedule_today[0].split(':')[1])) <= current_date.time() < time(
    hour=int(schedule_today[1].split(':')[0]), minute=int(schedule_today[1].split(':')[1])):
    dt = datetime(current_date.year, current_date.month, current_date.day, hour=int(schedule_today[1].split(':')[0]),
                  minute=int(schedule_today[1].split(':')[1]))
    print((dt - current_date).seconds // 60)
else:
    print('Магазин не работает')
