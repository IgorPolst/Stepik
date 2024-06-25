# объявление функции
def print_fio (name, sername, patronymic):
    print(sername[0].title(), name[0].title(), patronymic[0].title(), sep="")

# считывание данные

name, sername, patronymic = input(), input(), input()

# вызываем функцию
print_fio (name, sername, patronymic)