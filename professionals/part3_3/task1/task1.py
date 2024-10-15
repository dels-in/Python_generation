from datetime import datetime

with open("diary.txt") as file:
    diary = file.read()
    reports = diary.split("\n\n")
    sorted_reports = sorted(reports, key=lambda x: datetime.strptime(x.split("\n")[0], "%d.%m.%Y; %H:%M"))
    print(*sorted_reports, sep="\n\n")