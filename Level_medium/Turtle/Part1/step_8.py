import turtle as t

def hexagon(side):
    for _ in range (2):
        t.forward(side)
        t.left(30)
        t.forward(side)
        t.left(150)

hexagon(50)