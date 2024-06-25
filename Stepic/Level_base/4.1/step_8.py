# Формат входных данных
# На вход программе подаются три числа, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи.

first = int(input())
second = int(input())
third = int(input())

if second - first == third - second:
    print("YES")
else:
    print("NO")
