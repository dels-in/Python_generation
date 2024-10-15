from datetime import datetime, timedelta

inp = list(map(int, input().split(':')))
td = timedelta(hours=inp[0], minutes=inp[1], seconds=inp[2])
print((td - timedelta(0)).seconds)
