from string import ascii_letters, ascii_uppercase, ascii_lowercase, digits


def verification(login, password, success, failure):
    if not any(map(lambda x: x in ascii_letters, password)):
        failure(login, "в пароле нет ни одной буквы")
    elif not any(map(lambda x: x in ascii_uppercase, password)):
        failure(login, "в пароле нет ни одной заглавной буквы")
    elif not any(map(lambda x: x in ascii_lowercase, password)):
        failure(login, "в пароле нет ни одной строчной буквы")
    elif not any(map(lambda x: x in digits, password)):
        failure(login, "в пароле нет ни одной цифры")
    else:
        success(login)
