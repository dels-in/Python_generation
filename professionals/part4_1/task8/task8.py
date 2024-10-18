import sys
from datetime import datetime

dates = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin.readlines()]

if dates == sorted(set(dates)):
    print('ASC')
elif dates == sorted(set(dates), reverse=True):
    print('DESC')
else:
    print('MIX')