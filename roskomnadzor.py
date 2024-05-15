str = input() + " запретил букву"
alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
        'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
for i in range(len(alph)):
    if alph[i] in str:
        print(str, alph[i])
        str = " ".join(str.replace(alph[i], '').split())
