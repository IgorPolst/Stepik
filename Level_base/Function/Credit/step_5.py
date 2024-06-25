# объявление функции
def get_shipping_cost(quantity):
    cost = 1000 + (quantity - 1) * 120
    return cost


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))
