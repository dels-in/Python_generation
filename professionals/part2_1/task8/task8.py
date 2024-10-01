def print_given(*args, **kwargs):
    for arg in args:
        print(arg, type(arg))

    for k, v in sorted(kwargs.items()):
        print(k, v, type(v))
