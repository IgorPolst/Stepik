# Формат входных данных
# На вход программе подаётся четыре целых числа.

# Формат выходных данных
# Программа должна вывести наименьшее из четырёх чисел.


first = int(input())
second = int(input())
third = int(input())
forsth = int(input())
if first > second:
    first = second
if first > third:
    first = third
if first > forsth:
    first = forsth
print(first)
