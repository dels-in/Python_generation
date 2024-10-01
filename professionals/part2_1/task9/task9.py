def convert(string):
    return [string.upper(), string.lower()][
               len(list(filter(lambda c: c.islower(), string))) >= len(list(filter(lambda c: c.isupper(), string)))]
