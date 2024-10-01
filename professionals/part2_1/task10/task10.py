def filter_anagrams(word, words):
    return list(filter(lambda w: sorted(list(w)) == sorted(list(word)), words))