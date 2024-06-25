import turtle as t


def rectangle(side):
    for _ in range(3):
        t.forward(side)
        t.left(60)


rectangle(int(input()))
