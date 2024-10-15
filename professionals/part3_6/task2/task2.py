import time


def get_the_fastest_func(funcs, arg):
    return min(funcs, key=lambda x: calculate_it(x, arg))


def calculate_it(func, *args):
    start_time = time.monotonic()
    res = func(args)
    end_time = time.monotonic()
    return (end_time - start_time)


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


funcs = [for_and_append, list_comprehension, list_function]
print(get_the_fastest_func(funcs, range(100_000)))