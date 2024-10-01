def spell(*args):
    args = list(map(str.lower, list(args)))
    keys = set(map(lambda x: x[0], args))
    dict = {}
    for arg in args:
        for key in keys:
            if arg.startswith(key):
                if key in dict:
                    dict[key] = max(dict[key], len(arg))
                else:
                    dict.update({key: len(arg)})
    return dict


