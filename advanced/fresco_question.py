import decimal

with open("answers.txt", "w") as output, open("goats.txt") as input:
    colours = {}
    cur_col = input.readline().strip()
    while cur_col != "GOATS":
        colours.update({cur_col: 0})
        cur_col = input.readline().strip()
    del colours["COLOURS"]

    goats = list(map(str.strip, input.readlines()))
    for goat in goats:
        colours[goat] += 1

    for goat, count in colours.items():
        if count > decimal.Decimal(0.07)*len(goats):
            print(goat, file=output)

