import turtle as t


def rectangle(side):

    for _ in range(4):
        t.left(60)
        t.forward(side)


rectangle(int(input()))
