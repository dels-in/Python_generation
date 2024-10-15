import time
from math import factorial                   # функция из модуля math

def get_the_fastest_func(funcs, arg):
    return min(funcs, key=lambda x: calculate_it(x, arg))


def calculate_it(func, *args):
    start_time = time.monotonic()
    res = func(*args)
    end_time = time.monotonic()
    return (end_time - start_time)


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


funcs = [factorial, factorial_recurrent, factorial_classic]
print(get_the_fastest_func(funcs, 900))
