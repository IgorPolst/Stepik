# объявление функции
def convert_to_python_case(text):
    mass = [i for i in text]
    mass[0] = mass[0].lower()
    
    while not text.islower():
        for i in range(1, len(mass)):
            if mass[i].isupper():
                mass[i] = mass[i].lower()
                mass.insert(i, "_")
            text = "".join(mass)
    return text


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))

# # объявление функции
# def convert_to_python_case(text):
#     new_text = ""
#     for el in text:
#         if not el == el.lower():  # проверяем, что элемент в верхнем регистре (пропускаем цифры)
#             new_text += "_" + el.lower()
#         else:
#             new_text += el
            
#     return new_text[1:]


# # считываем данные
# txt = input()

# # вызываем функцию
# print(convert_to_python_case(txt))