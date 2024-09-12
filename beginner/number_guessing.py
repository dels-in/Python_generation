import random


def is_valid(number, right):
    if not number.isdigit():
        return False
    return 1 <= int(number) <= right


flag = True
while flag:
    right_inp = int(input("Введите правую границу выборки\n"))
    count = 0

    random = random.randrange(1, right_inp)
    print("Добро пожаловать в числовую угадайку")

    while True:
        n = input(f"Введите число от 1 до {right_inp}\n")

        if not is_valid(n, right_inp):
            print(f"А может быть все-таки введем целое число от 1 до {right_inp}?")
            continue

        n = int(n)
        count += 1

        if n < random:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif n > random:
            print("Ваше число больше загаданного, попробуйте еще разок")
        else:
            print("Вы угадали, поздравляем!")
            break

    print(f"Попыток потребовалось: {count}")
    print("Спасибо, что играли в числовую угадайку. Еще увидимся...")

    while True:
        again = input("Сыграем еще раз? (введите 'да' или 'нет')\n").lower()
        if again == "да":
            break
        elif again == "нет":
            flag = False
            break
        else:
            print("Введите 'да' или 'нет'")
