from datetime import timedelta, datetime

pattern = '%H:%M:%S'
dt = datetime.strptime(input(), pattern)
n = timedelta(seconds=int(input()))

print((dt + n).strftime(pattern))
