import turtle as t


def hexagon(side):
    n = 0
    for _ in range (100):
        for _ in range(4):
            t.backward(side+n)
            t.right(90)
        n+= 10


hexagon(50)