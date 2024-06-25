# объявление функции
def is_magic(date):
    mass = [int (i) for i in date.split(".")]
    return mass[0]*mass[1] == mass[2]%100

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))