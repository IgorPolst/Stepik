from math import sqrt, sinh
def pows(number):
    return number**2

def cub(number):
    return number**3

def root(number):
    return sqrt(number)

def mod(number):
    return abs(number)

def si(number):
    return sinh(number)

fun_dic = {"квадрат":pows, "куб":cub,"корень":root, "модуль":mod, "синус":si }
number, name = input(), input()

print(fun_dic[name](int(number)))