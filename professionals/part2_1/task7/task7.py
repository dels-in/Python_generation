def is_valid(string):
    return 3 < len(string) < 7 and string.isdigit() and string.find(" ") == -1
