numbers = list(map(int, input().split()))

s = set()

for number in numbers:
    if numbers.count(number) > 1:
        s.add(number)

print(*sorted(s))
