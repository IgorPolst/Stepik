# Формат входных данных
# На вход программе подаются три целых числа.

# Формат выходных данных
# Программа должна вывести одно число – сумму положительных чисел.

first = int(input())
second = int(input())
third = int(input())
summ = 0 
if first > 0:
    summ = summ + first
if second > 0:
    summ = summ + second
if third > 0:
    summ = summ + third
print (summ)