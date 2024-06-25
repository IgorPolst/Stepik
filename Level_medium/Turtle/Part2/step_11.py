import turtle as t


def circle(x, y, color):
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.circle(30)
    t.penup()


t.penup()
t.speed(5)
t.pensize(5)
circle(30, -20, "green")
circle(60, 15, "red")
circle(0, 15, "black")
circle(-60, 15, "blue")
circle(-30, -20, "yellow")
