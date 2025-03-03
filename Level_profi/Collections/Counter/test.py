from collections import Counter

# pets = Counter(cat=3, dog=3, fox=2, hamster=1)

# print(pets['elephant'])
# print(*pets)

# letters = Counter(set('Beautiful is better than ugly'))

# print(letters['t'])

# vegetables1 = Counter({'cabbage': 'ten', 'pepper': 'seven', 'pumpkin': 'four'})
# vegetables2 = Counter({'cabbage': 3, 'pepper': 2})

# vegetables1.update(vegetables2)

# print(vegetables1['pepper'])

# vegetables = Counter({'cabbage': 10, 'pepper': 'seven', 'pumpkin': 'four'})

# vegetables.update({'cabbage': 5, 'pepper': 'two'})

# print(vegetables['pepper'])
# print(vegetables['cabbage'])


# clothes = Counter([('shirt', 3), ('dress', 1), ('shirt', 3)])

# print(clothes['shirt'])

from collections import Counter

letters1 = Counter(a=1, b=-2, c=3, d=-4)

letters2 = +letters1
letters3 = -letters2

print(letters3)


# letters1 = Counter('stepik')
# letters2 = {'s': 1, 't': 1, 'e': 1, 'p': 1, 'i': 1, 'k': 1}

# print(letters1 + letters2)

word = 'stepik'

counter1 = Counter(word)
counter2 = Counter(word * 3)

print(counter1 < counter2)