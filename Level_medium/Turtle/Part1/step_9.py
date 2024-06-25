import turtle as t


def hexagon(side):
    t.left(30)
    for _ in range(2):
        t.forward(side)
        t.left(50)
        t.forward(side)
        t.left(130)


for _ in range(12):
    hexagon(50)
