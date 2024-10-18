import csv


def csv_columns(filename):
    with open(filename, 'r') as file:
        rows = csv.DictReader(file)
        d = {}
        for row in rows:
            for key, value in row.items():
                d[key] = d.get(key, []) + [value]
        return d