import turtle

window = turtle.Screen()


def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)


def figure(side, count):
    for _ in range(count):
        square(side)
        turtle.left(360 / count)


side, count = int(input()), int(input())

figure(side, count)

window.mainloop()  # не даст закрыть окно
