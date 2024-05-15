def pascal(n):
    list = [[1]]
    for i in range(1, n):
        for j in range(1, i + 1):
            if j == 1:
                list.append([1])
            elif i != 1 and j != 1:
                list[i].extend([list[i - 1][j - 1] + list[i - 1][j - 2]])
            if j == i:
                list[i].extend([1])
    return list


a = int(input())
pascal_triangle = pascal(a)

for str in pascal_triangle:
    print(*str)
