# Выбор и возврат необходимых словарей
def alpha(lang):
    # Английский алфавит
    const_upper_en = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    const_lower_en = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

    # Русский алфавит
    const_upper_ru = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    const_lower_ru = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"

    if lang == "en":
        return const_lower_en, const_upper_en
    else:
        return const_lower_ru, const_upper_ru


# Шифровка и дешифровка текста
# При шифровке выводится стандартный алфавит
# При дешифровке выводиться алфавит в обратном порядке


def chifer_dechifer(revers, lang):
    if revers == "1":
        return alpha(lang)
    else:
        lower, upper = alpha(lang)
        lower, upper = lower[::-1], upper[::-1]
        return lower, upper


def chifer_Cesar(text, dechifer, language):
    # Реализация шифра Цезаря
    cipher = ""
    alpha_lower, alpha_upper = chifer_dechifer(dechifer, language)
    for i in range(len(text)):
        if text[i] in alpha_lower:
            cipher += alpha_lower[alpha_lower.find(text[i]) + shift]
        elif text[i] in alpha_upper:
            cipher += alpha_upper[alpha_upper.find(text[i]) + shift]
        else:
            cipher += text[i]
    return text, cipher


# Работа с пользователем
search_key = input(
    "Известен ли вам сдвиг шифра да - 2, сдвиг = длинне слова - 1, нет - 0 : "
)
dechifer = input("Вам нужно зашифровать - 0 или дешифровать - 1 : ")
if search_key == "2":
    shift = int(input("Введите сдвиг "))
language = input("Выбирите язык en или ru: ")
text = input("Введите текст, который необходимо закоировать ")
if search_key == "1":
    word = [i for i in text.split(" ")]


if search_key == "2":
    # Преобразование с известным ключём
    text, cipher = chifer_Cesar(text, dechifer, language)
    print(f"Ваш текст \n{text} \nбыл приобразован \n{cipher}")
elif search_key == "1":
    # Ключом к шифру является длинна слова
    new_text = ""
    for i in word:
        shift = len(i)
        i, cipher = chifer_Cesar(i, dechifer, language)
        new_text += " " + cipher
    print(f"Ваш текст \n{text} \nбыл зашифрован в \n{new_text}")
else:
    # Перебор всех возможных вариантов расшифровки
    if dechifer == "0":
        print("Ваш текст может быть зашифрован: ")
    else:
        print("Ваш текст может быть дешифрован: ")
    upper, lower = alpha(language)
    for shift in range(1, len(upper) // 2):
        text, cipher = chifer_Cesar(text, dechifer, language)
        print(cipher)
