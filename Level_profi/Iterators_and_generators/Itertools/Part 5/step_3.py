from itertools import combinations_with_replacement

wallet = [100, 50, 20, 10, 5]

result = sorted(set(
    j for i in range(21)  # r должен быть от 1 до 16
    for j in combinations_with_replacement(wallet, r=i)
    if sum(j) == 100  # Суммируем элементы кортежа
))

print(len(result))

