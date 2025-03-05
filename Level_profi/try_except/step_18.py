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
    if not (string != string.upper() and string != string.lower()):
        raise LetterError
    if not any(i.isdigit() for i in string):
        raise DigitError

    return True


door = True

while door:
    try:
        is_good_password(input())
    except LengthError:
        print("LengthError")
    except LetterError:
        print("LetterError")
    except DigitError:
        print("DigitError")
    else:
        door = False
        print("Success!")
