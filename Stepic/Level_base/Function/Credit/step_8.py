# объявление функции
def get_month(language, number):
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == "ru":
        return lng_ru[number-1]
    else:
        return lng_en[number-1]
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))