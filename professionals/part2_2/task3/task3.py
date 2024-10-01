def add_reverse(start_index, end_index, list):
    list[start_index-1:end_index] = list[start_index-1:end_index][::-1]
    return list


n, X, Y, A, B = map(int, input().split())

res = list(range(1, n + 1))

res = add_reverse(X, Y, res)
res = add_reverse(A, B, res)

print(*res)
