import turtle as t
t.colormode(255)
t.bgcolor('black')
t.speed(10)
t.penup()
t.shape('turtle')
r = 0
g = 0 
b = 255
for i in range(1, 1000): 
    if 0 < i % 379 < 64: 
        r += 4
    elif 63 < i % 379 < 127: 
        b -= 4 
    elif 126 < i % 379 < 190: 
        g += 4
    elif 189 < i % 379 < 253:
        r -= 4
    elif 252 < i % 379 < 316:
        b += 4
    elif 315 < i % 379 < 379:
        g -= 4
    t.color((0, 0, 0), (r, g, b)) 
    t.stamp()
    t.left(22)
    t.forward(1.01 ** i)
  
t.mainloop()