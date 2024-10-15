from datetime import date, time

dates = [input() for _ in range(int(input()))]

print(*map(lambda x: date.fromisoformat(x).strftime("%d/%m/%Y"), sorted(dates)), sep='\n')
