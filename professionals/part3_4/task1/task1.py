from datetime import date, datetime, timedelta

current = datetime.strptime(input(), "%d.%m.%Y")
print((current - timedelta(days=1)).strftime("%d.%m.%Y"))
print((current + timedelta(days=1)).strftime("%d.%m.%Y"))
