def to_sublist(str):
    str = str.split()
    sublist = [[]]
    for i in range(len(str)):
        for j in range(len(str) - i):
            sublist.append(str[j:j + i + 1])
    return sublist


s = input()
string = to_sublist(s)

print(string)
