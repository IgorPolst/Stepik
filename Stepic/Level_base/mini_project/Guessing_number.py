# Используемые библиотеки
from random import randint


# Объявление функций
def is_vailed(num):  # Проверка введённых данных на пригодность
    return num.isdigit() and 1 <= int(num) <= 100


def game_body(search_number, number, total):  # Сама игра
    while search_number != number:
        if is_vailed(number):
            number = int(number)
            if number < search_number:
                print("Ваше число меньше заданного, попробуйте ещё разок")
                total += 1
            elif number > search_number:
                print("Ваше число больше заданного, попробуйте ещё разок")
                total += 1
            else:
                total += 1
                print("Вы угадали, поздравляю!")
                print(f"Вам потребовалось {total} попыток")
                print(f"Сыграем ещё? Да - Y Нет - N ", exiter=input())

        else:
            print("Это не то что нам нужно! Прочтите внимательно!")
        number = input()


total = 0
exiter = "Y"
print("Добро пожаловать в числовую угадайку!")

# Организация второй игры
while exiter == "Y":
    print("Пожалуйста ввежите число от 1 до 100:")
    number = input()
    if total == 0:
        search_number = randint(1, 100)
        game_body(search_number, number, total)
    else:
        total = 0
        search_number = randint(1, 100)
        game_body(search_number, number, total)


print("Спасибо, что играли в числовую угадайку. Ещё увидимся!)")
