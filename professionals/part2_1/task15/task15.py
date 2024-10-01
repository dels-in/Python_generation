def get_biggest(numbers):
    if len(numbers) == 0:
        return -1
    numbers = list(map(str, numbers))
    biggest = ""

    for _ in range(len(numbers)):
        m_l = max(map(lambda x: len(x), numbers))
        m = str(max(numbers, key=lambda x: x * m_l))
        biggest += m
        numbers.remove(m)
    return int(biggest)
