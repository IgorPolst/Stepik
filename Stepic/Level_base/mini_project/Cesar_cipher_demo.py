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


word = [i for i in input().split(" ")]
print(word)
new_text = ""

for i in word:
    count = 0
    for j in i:
        if j.isalpha():
            count += 1
    shift = count
    i, cipher = chifer_Cesar(i, "1", "ru")
    new_text += cipher + " "
print(word, "\n", new_text)
