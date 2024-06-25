import turtle as t

# Отрисовка сигнала светофора
def circle11 (x,y, color):
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()

# Отрисовка корпуса светофора
t.Screen().setup(1000, 500)
t.hideturtle()
t.begin_fill()
for _ in range (2):
    t.forward(100)
    t.right(90)
    t.forward(280)
    t.right(90)
t.end_fill()

t. penup()
circle11(50,-90, "red")
circle11(50,-180, "yellow")
circle11(50,-270, "green")


