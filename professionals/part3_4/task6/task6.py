from datetime import timedelta, datetime

dates = [datetime.strptime(i, '%d.%m.%Y') for i in input().split()]

res = []
for i in range(1, len(dates)):
    res.append(abs((dates[i] - dates[i - 1]).days))

print(res)