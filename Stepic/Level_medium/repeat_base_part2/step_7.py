mass = ["камень", "ножницы", "бумага"]
name = ["Тимур", "Руслан", "ничья"]

first, second = input(), input()


def stone(second):
    if second == "ножницы" or second == "ящерица":
        return 0
    elif second == "бумага" or second == "Спок":
        return 1
    else:
        return 2


def scissors(second):
    if second == "бумага" or second == "ящерица":
        return 0
    elif second == "камень" or second == "Спок":
        return 1
    else:
        return 2


def paper(second):
    if second == "камень" or second == "Спок":
        return 0
    elif second == "ножницы" or second == "ящерица":
        return 1
    else:
        return 2


def lizard(second):
    if second == "Спок" or second == "бумага":
        return 0
    elif second == "камень" or second == "ножницы":
        return 1
    else:
        return 2


def Spok(second):
    if second == "ножницы" or second == "камень":
        return 0
    elif second == "ящерица" or second == "бумага":
        return 1
    else:
        return 2


if first == "камень":
    print(name[stone(second)])
elif first == "ножницы":
    print(name[scissors(second)])
elif first == "бумага":
    print(name[paper(second)])
elif first == "ящерица":
    print(name[lizard(second)])
elif first == "Спок":
    print(name[Spok(second)])
