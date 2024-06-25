langes = {}
n = int(input())
for _ in range(n):
    for lang in input().split():
        langes[lang.strip(", ")] = langes.setdefault(lang.strip(", "), 0)+1
result = list(map(lambda x: x[0],filter(lambda count: n == count[1],langes.items())))
if result == []:
    print("Сериал снять не удастся")
else: 
    print(*sorted(result), sep =", ")

# Код профи 
# n = int(input())
# langs = set(input().split(', '))

# for _ in range(n - 1):
#     langs &= set(input().split(', '))

# if langs:
#     print(*sorted(langs), sep=', ')
# else:
#     print('Фильм снять не удастся')