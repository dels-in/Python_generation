with open("forbidden_words.txt") as forb, open("data.txt") as file:
    forb_words = list(map(str.strip, forb.read().split()))
    for line in file:
        l_line = line.lower()
        for word in forb_words:
            if word in l_line:
                l_line = l_line.replace(word, "*" * len(word))

        for i in range(len(l_line)):
            if l_line[i] == "*":
                print(l_line[i], end="")
            else:
                print(line[i], end="")
