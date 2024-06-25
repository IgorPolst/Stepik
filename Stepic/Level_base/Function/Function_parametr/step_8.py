# объявление функции
def draw_triangle(fill, base):
    for i in range (1, base//2+1):
        print(fill*i)
    for i in range (base//2+1):
        print(fill*(base//2+1-i))
# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)

# # объявление функции
# def draw_triangle(fill, base):
#     for i in range(base // 2):
#         print(fill * (i + 1))

#     for i in range(base // 2, -1, -1):
#         print(fill * (i + 1))


# # считываем данные
# fill = input()
# base = int(input())

# # вызываем функцию
# draw_triangle(fill, base)