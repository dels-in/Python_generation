import sys

moves = [int(line) for line in sys.stdin.readlines()]

print(['Дима', 'Анри'][
          (moves[-1] % 2 == 0 and (len(moves) - moves[::-1].index(moves[-1])) % 2 == 1) or ((len(moves) - moves[::-1].index(
              moves[-1])) % 2 == 0 and moves[-1] % 2 == 1)])
