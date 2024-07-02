from datetime import datetime, timedelta

def choose_plural(amount, declensions):
    if amount % 10 in [0, 5, 6, 7, 8, 9] or amount % 100 in [11, 12, 13, 14]:
        koin = 2
    elif amount % 10 == 1:
        koin = 0
    elif amount % 10 in [2, 3, 4]:
        koin = 1

    return f"{amount} {declensions[koin]}"

present_time = datetime(2022,11,8,12,0)
today = datetime.strptime(input(), "%d.%m.%Y %H:%M")
delta = present_time - today


day = ['день', "дня", "дней"]
hour = ['час', 'часа', 'часов']
minute = ['минута', 'минуты', 'минут']


if delta.seconds <= 0:
    print("Курс уже вышел!")
elif delta.seconds < 3600: 
    print(f"До выхода курса осталось: {choose_plural(delta.seconds//60,minute)}")
elif delta.seconds < 86400 and delta.seconds%3600 == 0:
    print(f"До выхода курса осталось: {choose_plural(delta.seconds // 3600 ,hour)}")
elif delta.seconds < 86400 and delta.seconds%3600 != 0:
    print(f"До выхода курса осталось: {choose_plural(delta.seconds // 3600 ,hour)} и {choose_plural(delta.seconds % 3600 // 60,minute)}")    
elif delta.seconds%86400 != 0: 
    print(f"До выхода курса осталось: {choose_plural(delta.days, day)} и {choose_plural(delta.seconds % 86400 // 3600,hour)}")


# from datetime import datetime

# def time_left(current_datetime):
#     release_datetime = datetime.strptime("08.11.2022 12:00", "%d.%m.%Y %H:%M")
    
#     if current_datetime >= release_datetime:
#         return "Курс уже вышел!"
    
#     time_difference = release_datetime - current_datetime
#     days = time_difference.days
#     hours, remainder = divmod(time_difference.seconds, 3600)
#     minutes = remainder // 60
    
#     if days > 0 and hours > 0:
#         return f"До выхода курса осталось: {days} {choose_plural(days, 'день', 'дня', 'дней')} и {hours} {choose_plural(hours, 'час', 'часа', 'часов')}"
#     elif days > 0:
#         return f"До выхода курса осталось: {days} {choose_plural(days, 'день', 'дня', 'дней')}"
#     elif hours > 0 and minutes > 0:
#         return f"До выхода курса осталось: {hours} {choose_plural(hours, 'час', 'часа', 'часов')} и {minutes} {choose_plural(minutes, 'минута', 'минуты', 'минут')}"
#     elif hours > 0:
#         return f"До выхода курса осталось: {hours} {choose_plural(hours, 'час', 'часа', 'часов')}"
#     else:
#         return f"До выхода курса осталось: {minutes} {choose_plural(minutes, 'минута', 'минуты', 'минут')}"

# def choose_plural(number, singular, plural, plural_genitive):
#     if number % 10 == 1 and number % 100 != 11:
#         return singular
#     elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
#         return plural
#     else:
#         return plural_genitive

# current_datetime = datetime.strptime(input(), "%d.%m.%Y %H:%M")
# print(time_left(current_datetime))