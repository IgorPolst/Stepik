# Формат входных данных
# На вход программе подаётся одно целое число.

# Формат выходных данных
# Программа должна вывести «Четное», если число четное, и «Нечетное» — если число нечетное.

number = int(input())
remains = number % 2
if remains == 0:
    print("Четное")
else:
    print("Нечетное")