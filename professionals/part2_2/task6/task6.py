langs = [input().split(", ") for _ in range(int(input()))]

s = set()
for lang in langs:
    for l in lang:
        s.add(l)

for lang in langs:
    s = s & set(lang)

if len(s) == 0:
    print("Сериал снять не удастся")
else:
    print(*sorted(s), sep=", ")
