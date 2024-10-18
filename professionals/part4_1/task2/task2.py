import sys, datetime

dates = [datetime.datetime.strptime(line.strip(), '%Y-%m-%d') for line in sys.stdin.readlines()]

print((max(dates) - min(dates)).days)
