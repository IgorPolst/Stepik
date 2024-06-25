import turtle as t

t.shape("turtle")
t.stamp()
t.penup()
n = 50
for _ in range(8):
    t.forward(n)
    t.stamp()
    t.backward(n)
    t.left(45)
