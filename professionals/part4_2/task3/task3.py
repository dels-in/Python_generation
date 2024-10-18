import csv

column_index = int(input())-1
with open('deniro.csv', 'r') as file:
    rows = list(csv.reader(file))
    rows.sort(key = lambda x: int(x[column_index]) if x[column_index].isdigit() else x[column_index])

    for row in rows:
        print(*row, sep=',', end='\n')
