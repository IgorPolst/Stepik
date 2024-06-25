import turtle as t


def hexagon(side):
    t.left(120)
    for _ in range(5):
        t.forward(side)
        t.left(144)


hexagon(50)
