import turtle as t

def circle (n, color):
    t.goto(-n,0)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(n)
    t.end_fill()
    t.penup()
n = 100
RGB = [(255, 38, 0), (255, 170, 0), (212, 250, 0), (49, 250, 0), (0, 250, 121), (0, 253, 255), (0, 128, 255), (68, 52, 255), (216, 60, 255), (255, 50, 169)]
t.Screen().setup(1000, 500)
t.hideturtle()
t.penup()
for i in range (10):
    color = RGB[i]
    t.circle(n,color)
    n -= 10