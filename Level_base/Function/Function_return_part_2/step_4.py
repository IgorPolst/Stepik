# объявление функции
def is_prime(num):
    flag = False
    while flag == False:
        num += 1
        total = 0
        for i in range(2, num):
            if num % i == 0:
                total += 1
        if total == 0:
            flag == True
            return num


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
