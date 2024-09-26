def read_csv():
    with open('data.csv', encoding='utf-8') as file:
        keys = file.readline().strip().split(',')
        return [dict(zip(keys, line.strip().split(','))) for line in file]


print(*read_csv(), sep="\n")
