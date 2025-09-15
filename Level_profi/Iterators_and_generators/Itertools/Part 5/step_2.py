from itertools import combinations

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

result = sorted(set(
    j for i in range(1, 17)  # r должен быть от 1 до 16
    for j in combinations(wallet, r=i)
    if sum(j) == 100  # Суммируем элементы кортежа
))

print(result)

