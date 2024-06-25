import turtle as t

t.pensize(2)
t.penup()
t.goto(0, -100)
t.pendown()

t.circle(100)
t.circle(50)

t.penup()
t.goto(-60, 80)
t.pendown()
t.circle(20)
t.penup()
t.goto(60, 80)
t.pendown()
t.circle(20)
t.penup()

t.shape("circle")
t.goto(-40, 10)
t.stamp()
t.goto(40, 10)
t.stamp()

t.goto(0, -80)
t.pendown()
t.left(90)
t.forward(50)
t.right(90)
t.circle(5)
t.hideturtle()
