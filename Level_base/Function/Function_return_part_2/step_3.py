# объявление функции
def is_prime(num):
    if num != 1:
        total = 0
        for i in range(1, num + 1):
            if num % i == 0:
                total += 1
        if total > 2:
            return False
        else:
            return True

    else:
        return False


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
