import sys

comments = [line for line in sys.stdin.readlines() if line.strip().startswith('#')]

print(len(comments))