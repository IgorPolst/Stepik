from turtle import *
import random as r


# начальные настройки черепашки, можно задать скрытие указателя, скорость,
# положение пера, вид указателя, позицию старта, размер пера, цвет фона, значение параметра tracer для быстрой отрисовки
def settings(show, sp, up, sh, pos, sz, b_col, trace):
    # show(True\False)|sp(int)|up(True\False)|sh(str)|pos(tuple)|sz(int)|b_col(str)
    if not show:
        hideturtle()
    if up:
        penup()
    Screen().colormode(255)  # нужно закомментировать для Trinket
    params = [speed(sp), shape(sh), goto(pos), pensize(sz), Screen().bgcolor(b_col), tracer(trace)]


# функция-алгоритм снежинки, принимает в параметры размер одного звена ветви,
# цвет, толщину и координаты старта
def snowflake(size, color, depth, dest):
    snowflake_defaults = [goto(dest), pencolor(color), pensize(depth), pd()]

    def branch():
        [(fd(size), lt(45), fd(size), bk(size), rt(90), fd(size), bk(size), lt(45)) for _ in
         range(4)]
        end_of_branch = [fd(size), bk(size * 5), lt(45)]

    [branch() for _ in range(8)]
    pu()


# основное тело программы реализовано в виде функции snowing()
def snowing():  # объявляем будущий словарь для хранения граничных значений отрисованных снежинок
    coordinates = {(0, 0): (0, 0, 0, 0)}  # назначаем точку отсчета для начала вычисления расположения снежинок
    attempt_counter = 0  # счетчик попыток генерации допустимых снежинок
    while attempt_counter < 10 ** 5 * 2:
        if attempt_counter > 10 ** 3:  # если неудачных попыток больше заданного числа,
            size_k = (3, 6)  # уменьшаем возможные размеры звеньев
        else:
            size_k = (5, 21)
        size = r.randrange(*size_k)  # задаем случайный размер звена в заданном диапазоне
        dest = (r.randint(-600, 600), r.randint(-300, 250))  # случайные координаты снежинки, диапазоны также служат
        # ограничением поля отрисовки, в моем случае для полноэкранного отображения при разрешении экрана 1440х900.
        math_coord = tuple([dest[i] + size * j for i in [0, 1] for j in [-5, 5]]) # вычисляем границы снежинки 
        # condition - правило для проверки корректности расположения снежинки - любую снежинку используемого типа можно
        # вписать в квадрат, граничные значения которого не должны пересекаться с уже имеющимися "квадратами",
        # занесенными в соответствующий словарь. Достаточно одного из граничных значений, но для каждой снежинки,
        # уже находящейся в словаре
        condition = [any([math_coord[0] > c[1], math_coord[1] < c[0], math_coord[2] > c[3],
                          math_coord[3] < c[2]]) for c in coordinates.values()]
        if all(condition):  # если случайная снежинка может быть размещена
            color = r.sample([c for c in range(1, 256)], 3)
            snowflake(size, color, size // 3, dest)  # рисуем снежинку
            coordinates[dest] = math_coord  # заносим координаты отрисованной снежинки в словарь
            if attempt_counter < 10 ** 4:
                attempt_counter = 0
            else:
                attempt_counter = 10 ** 4  # генерируем только маленькие снежинки
        else:
            attempt_counter += 1
    goto(0, 350)
    pencolor(*r.sample([c for c in range(1, 256)], 3))
    write('Sorry, not enough space for a new snowflake', align='center', font=('Garamond', 40, 'italic'))
    # по завершении цикла рисуем сообщение об отсутсвии свободных мест для снежинок


settings(False, 0, True, 'turtle', (0, 0), 2, 'lightskyblue', 2)
snowing()

end = input('For exit enter any character\n')