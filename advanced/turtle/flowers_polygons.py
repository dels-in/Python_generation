import turtle

window = turtle.Screen()


def polygon(side, count):
    for _ in range(count):
        turtle.forward(side)
        turtle.left(360/count)

def flower(side, count):
    for _ in range(count):
        turtle.right(180-360/count)
        polygon(side, count)
        turtle.left(180-360/count)
        turtle.forward(side)
        turtle.left(360/count)


side, count = int(input()), int(input())

flower(side, count)

window.mainloop()  # не даст закрыть окно
