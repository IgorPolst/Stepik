from turtle import *
bgcolor('darkblue'), penup(), speed(0)  # Настройка основных значений
dot(200, 'gold3'), forward(200)  # Рисование луны
shape('circle'), shapesize(10), color('darkblue')  # Настройка вида черепашки
while True:  # Цикл прохода черепашки справа налево
    for _ in range(400):
        backward(1)
    forward(400)