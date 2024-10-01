d1, d2, d3 = input(), input(), input()

l = list(map(int, [d1, d2, d3]))

if max(l) < sum(l) - max(l):
    print(sum(l))
else:
    print((sum(l) - max(l)) * 2)
