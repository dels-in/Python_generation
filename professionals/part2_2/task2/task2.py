chars = [input() for _ in range(3)]
eng = "AaBCcEeHKMOoPpTXxy"
ru = "АаВСсЕеНКМОоРрТХху"

if all(map(lambda x: x in eng, chars)):
    print("en")
elif all(map(lambda x: x in ru, chars)):
    print("ru")
else:
    print("mix")



