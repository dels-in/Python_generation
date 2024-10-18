import csv

with open('salary_data.csv', 'r') as file:
    rows = csv.DictReader(file, delimiter=';')
    salaries = {}
    for row in rows:
        salaries[row['company_name']] = salaries.get(row['company_name'], '0') + ' ' + row['salary']

    mean_salaries = {}
    for company in salaries:
        int_salaries = list(map(int, salaries[company].split()))
        mean_salaries[company] = sum(int_salaries) / len(int_salaries)

    print(*sorted(mean_salaries, key=lambda s: (mean_salaries[s], s)), sep='\n')
