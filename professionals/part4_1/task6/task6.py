import sys

comments = [line for line in sys.stdin.readlines() if not line.strip().startswith('#')]

for line in comments:
    print(line, end='')