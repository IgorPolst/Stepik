# from collections import namedtuple
# from  itertools import combinations

# Item = namedtuple('Item', ['name', 'mass', 'price'])

# items = [Item('Обручальное кольцо', 7, 49_000),
#          Item('Мобильный телефон', 200, 110_000),
#          Item('Ноутбук', 2000, 150_000),
#          Item('Ручка Паркер', 20, 37_000),
#          Item('Статуэтка Оскар', 4000, 28_000),
#          Item('Наушники', 150, 11_000),
#          Item('Гитара', 1500, 32_000),
#          Item('Золотая монета', 8, 140_000),
#          Item('Фотоаппарат', 720, 79_000),
#          Item('Лимитированные кроссовки', 300, 80_000)]
# res_mass = int(input())
# res = []
# items_combination = combinations(items)
# for comb in items_combination:
#     if sum([it.mass for it in comb]) <= res_mass:
#         res += comb

# max(res, key=lambda comb: for it)

from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49000),
         Item('Мобильный телефон', 200, 110000),
         Item('Ноутбук', 2000, 150000),
         Item('Ручка Паркер', 20, 37000),
         Item('Статуэтка Оскар', 4000, 28000),
         Item('Наушники', 150, 11000),
         Item('Гитара', 1500, 32000),
         Item('Золотая монета', 8, 140000),
         Item('Фотоаппарат', 720, 79000),
         Item('Лимитированные кроссовки', 300, 80000)]

capacity = int(input())

res = []
max_price = 0

# Перебираем все сочетания предметов
for r in range(1, len(items) + 1):
    for comb in combinations(items, r):
        total_mass = sum(it.mass for it in comb)
        total_price = sum(it.price for it in comb)
        if total_mass <= capacity and total_price > max_price:
            max_price = total_price
            res = comb

if not res:
    print("Рюкзак собрать не удастся")
else:
    for name in sorted(it.name for it in res):
        print(name)
