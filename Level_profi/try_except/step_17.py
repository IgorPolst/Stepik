class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    if any(i.isdigit() for i in string):
        raise DigitError

    if string != string.upper() and string != string.lower():
        raise LetterError
    return True


try:
    print(is_good_password("Short7"))
except Exception as err:
    print(type(err))
