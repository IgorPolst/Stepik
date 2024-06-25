# объявление функции
def is_password_good(password):
    if (
        len(password) >= 8
        and not password.islower()
        and not password.isupper()
        and not password.isalpha()
        and not password.isdigit()

    ):
        flag = False
        for i in password:
            if i in "0123456789":
                flag = True
        if flag:
            return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
