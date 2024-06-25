# На вход программе подаются два натуральных числа 
# a и b. Напишите программу с использованием встроенной функции all() для обнаружения всех целых чисел в диапазоне 
# [a;b], которые делятся на каждую содержащуюся в них цифру без остатка.

def check_divisibility(number):
    for digit in str(number):
        if int(digit) != 0 and number % int(digit) != 0 or int(digit) == 0:
            return False
    return True

a = int(input())
b = int(input())

#numbers = [i for i in range(a, b+1) if all(check_divisibility(i))]
numbers = []
for i in range (a, b+1):
    if check_divisibility(i):
        numbers.append(i)
        
print(*numbers)

# a, b = int(input()), int(input())

# for i in range(a, b + 1):
#     # создаем кортеж со всеми цифрами числа
#     digits = tuple(map(int, str(i)))
    
#     # проверяем, что число не содержит 0 и делится на все свои цифры
#     if 0 not in digits and all(map(lambda cur_digit: i % cur_digit == 0, digits)):
#         print(i, end=" ")