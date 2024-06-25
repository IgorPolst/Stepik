from random import randrange

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."

chars = ""
exiter = "Y"

while exiter != "N":
    number_password = int(input("Пожалуйста введите количество необходимых паролей "))
    len_password = int(input("Пожалуйста введите длину необходимых вам паролей "))
    flag_digit = bool(input("Нужны ли цифры в вашем пароле True or False "))
    flag_uppercase = bool(
        input("Нужны ли прописные буквы в вашем пароле True or False ")
    )
    flag_lowerrcase = bool(
        input("Нужны ли строчные букву в вашем пароле True or False ")
    )
    flag_punctuation = bool(input("Нужны ли символы в вашем пароле True or False "))
    for i in range(number_password):
        j = 0
        while j < len_password:
            choice = randrange(4)
            if choice == 0 and flag_digit:
                chars += digits[randrange(len(digits))]
                j += 1
            elif choice == 1 and flag_lowerrcase:
                chars += lowercase_letters[randrange(len(lowercase_letters))]
                j += 1
            elif choice == 2 and flag_uppercase:
                chars += uppercase_letters[randrange(len(uppercase_letters))]
                j += 1
            elif choice == 3 and flag_punctuation:
                chars += punctuation[randrange(len(punctuation))]
                j += 1
        print(f"Ваш {i} пароль: ", chars)
        chars = ""
    exiter = input("Хотите сгенерироваать другие пароли Да - Y Нет - N ")

print("Спаибо что пользуетесь нашей программой.")
