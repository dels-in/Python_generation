from functools import reduce


def evaluate(coefficients, x):
    formula = list(map(lambda coef, i: coef * x ** i, coefficients, range(len(coefficients)-1, -1, -1)))
    return reduce(lambda num1, num2: num1 + num2, formula, 0)


def evaluate1(coefficients, x):
    res = 0
    for i in range(len(coefficients)):
        res += coefficients[i] * x ** (len(coefficients) - i - 1)
    return res


coefficients, x = [int(i) for i in input().split()], int(input())

print(evaluate(coefficients, x))
print(evaluate1(coefficients, x))
