import turtle as t

t.color("red")
t.dot()
t.right(180)
n = 0
for _ in range(10):
    t.color("green")
    t.goto(-250 + n, -100)
    t.color("blue")
    t.dot()
    t.color("green")
    t.goto(0, 0)
    n += 50
