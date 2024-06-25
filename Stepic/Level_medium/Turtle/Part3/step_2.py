import turtle as t

t.Screen().setup(400, 300)
t.hideturtle()
t.fillcolor("blue")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-10,100)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
for _ in range(4):
    t.forward(120)
    t.left(120)
t.end_fill()