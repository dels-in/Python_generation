import sys

numbers = [int(line) for line in sys.stdin.readlines()]

if sum(numbers) == (numbers[0]+numbers[-1])/2*len(numbers):
    print('Арифметическая прогрессия')
elif sum(numbers) == numbers[0]*((numbers[1]/numbers[0])**len(numbers)-1)/(numbers[1]/numbers[0]-1):
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')