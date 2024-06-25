# объявление функции
def is_pangram(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in abc:
        if i not in text.lower():
            return False
    return True


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
