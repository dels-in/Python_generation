def index_of_nearest(numbers, number):
    if len(numbers) == 0:
        return -1
    else:
        return numbers.index(min(numbers, key=lambda x: abs(x - number)))


