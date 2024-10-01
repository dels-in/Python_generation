occupied_names = [input() for _ in range(int(input()))]
m = int(input())
new_names = [input() for _ in range(m)]

for i in range(len(new_names)):
    if new_names[i] + "@beegeek.bzz" not in occupied_names:
        occupied_names.append(new_names[i] + "@beegeek.bzz")
    elif new_names[i] + "@beegeek.bzz" in occupied_names:
        count = 1
        while new_names[i] + str(count) + "@beegeek.bzz" in occupied_names:
            count += 1
        a = new_names[i] + str(count) + "@beegeek.bzz"
        occupied_names.append(new_names[i] + str(count) + "@beegeek.bzz")

print(*occupied_names[-m:], sep="\n")
