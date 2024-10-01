n = int(input())
numbers = list(range(1, n + 1))

sums = list(map(lambda x: sum(map(int, str(x))), numbers))

print(max(map(lambda x: sums.count(x), sums)))