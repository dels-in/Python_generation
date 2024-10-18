import sys

lines = sys.stdin.readlines()
for line in lines:
    print(line.strip()[::-1])