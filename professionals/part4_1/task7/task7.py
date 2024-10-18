import sys

news = [line.split(' / ') for line in sys.stdin.readlines()]
category = news.pop()[0].strip()

res_news = []
for line in news:
    if line[1] == category:
        res_news.append((float(line[2]), line[0]))

for res in sorted(res_news):
    print(res[1], sep='')
