def choose_plural(amount, declensions):
    if amount > 9:
        if str(amount)[-1] == "1" and str(amount)[-2] != "1":
            return f'{amount} {declensions[0]}'
        elif str(amount)[-1] in "234" and str(amount)[-2] != "1":
            return f'{amount} {declensions[1]}'
        else:
            return f'{amount} {declensions[2]}'

    else:
        if str(amount)[-1] == "1":
            return f'{amount} {declensions[0]}'
        elif str(amount)[-1] in "234":
            return f'{amount} {declensions[1]}'
        else:
            return f'{amount} {declensions[2]}'
