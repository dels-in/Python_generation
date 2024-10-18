import csv

with open('tests/sales.csv', 'r') as file:
    rows = csv.DictReader(file, delimiter=';')
    for row in rows:
        if int(row['new_price']) < int(row['old_price']):
            print(row['name'])