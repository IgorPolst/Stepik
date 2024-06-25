# объявление функции
def find_all(target, symbol):
    mass = []
    for i in range(len(target)):
        if target[i] == symbol:
            mass.append(i)
    return mass


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
