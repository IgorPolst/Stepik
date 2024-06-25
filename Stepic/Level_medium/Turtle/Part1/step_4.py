import turtle as t


def rectangle(side, angle):
    for _ in range(100):
        t.left(angle)
        for _ in range(4):
            t.forward(side)
            t.left(90)


rectangle(int(input()), int(input()))
