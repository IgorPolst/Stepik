import turtle as t

t.shape("turtle")
t.stamp()
t.penup()
n = 50
for _ in range(8):
    t.forward(n * (2 / 3))
    t.pendown()
    t.forward(n * (1 / 3))
    t.penup()
    t.stamp()
    t.backward(n)
    t.left(45)
