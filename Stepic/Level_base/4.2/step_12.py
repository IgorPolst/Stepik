# Формат входных данных
# На вход программе подаётся три положительных целых числа.

# Формат выходных данных
# Программа должна вывести «YES» или «NO» в соответствии с условием задачи.

first = int(input())
second = int(input())
third = int(input())

if first + second > third and first + third > second and second + third > first:
    print("YES")
else:
    print("NO")
