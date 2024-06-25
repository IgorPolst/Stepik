import turtle as t


def hexagon(side):
    t.forward(side)
    t.backward(side * 2)
    t.forward(side)
    t.left(30)


for _ in range(6):
    hexagon(50)
