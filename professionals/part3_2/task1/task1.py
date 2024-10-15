from datetime import date, time

d1, d2 = date.fromisoformat(input()), date.fromisoformat(input())

print(min(d1, d2).strftime("%d-%m (%Y)"))

# Вариант 2

# print(date.fromisoformat(min(input(), input())).strftime("%d-%m (%Y)"))
