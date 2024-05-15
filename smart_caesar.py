def encode(text):
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    words = text.split()
    res=[]
    for word in words:
        str = ""
        w = [i for i in word if i.isalpha()]
        step = len(w)
        for i in range(len(word)):
            alphas = 26
            low_alphabet = lower_eng_alphabet
            upp_alphabet = upper_eng_alphabet

            if word[i].isalpha():
                if word[i] == word[i].lower():
                    place = low_alphabet.index(word[i])
                if word[i] == word[i].upper():
                    place = upp_alphabet.index(word[i])

                index = (place + int(step)) % alphas

                if word[i] == word[i].lower():
                    str += low_alphabet[index]
                if word[i] == word[i].upper():
                    str += upp_alphabet[index]

            else:
                str+=word[i]
        res.append(str)
    return " ".join(res)


print(encode(input()))
