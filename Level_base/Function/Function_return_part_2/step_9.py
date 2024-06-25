# объявление функции
def is_correct_bracket(text):
    total = 0
    for i in text:
        if i == "(":
            total += 1
        if i == ")":
            total -= 1
        if total < 0:
            return False
    return total == 0


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
