# объявление функции
def factorial(fac):
    result = 1
    for i in range(1, fac + 1):
        result *= i
    return result


def compute_binom(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(int(compute_binom(n, k)))
