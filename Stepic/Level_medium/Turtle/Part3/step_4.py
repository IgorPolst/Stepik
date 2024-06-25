import turtle as t

def circle (x,y):
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.penup()

def triangle1(x,y,n):
    t.goto(x,y)
    t.pendown()
    if n == 0:
        t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()       
    t.penup()

t.penup()
circle(50,50)
circle(-50,50)
circle(0,-75)
triangle1(-50,0,1)
t.left(60)
triangle1(0,-50,0)