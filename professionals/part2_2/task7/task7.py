word = input()
words = [input() for _ in range(int(input()))]

gl = "а, у, о, ы, и, э, я, ю, ё, е".split(", ")
sogl = "б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ".split(", ")

gl_indexes_word = [i for i, ltr in enumerate(word) if ltr in gl]

for w in words:
    gl_indexes_w = [i for i, ltr in enumerate(w) if ltr in gl]
    if gl_indexes_word == gl_indexes_w:
        print(w)
