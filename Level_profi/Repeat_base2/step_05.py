numbers = [int(i) for i in range(int(input()) + 1)]
summ = list(map(lambda x: sum(map(int, str(x))), numbers))
print(max(map(lambda x: summ.count(x), summ)))
