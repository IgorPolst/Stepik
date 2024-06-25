import turtle as t


t.shape("circle")
t.stamp()
n = 50
for _ in range(1000):
    t.shape("arrow")
    t.forward(n)
    t.stamp()
    t.backward(n)
    t.left(0.9)
