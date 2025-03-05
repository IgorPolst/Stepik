class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string):
    if len(string)  < 9:
        raise LengthError
    if any(i.isdigit() for i in string):
        raise DigitError

    if (string != string.upper()
        and string != string.lower()):
        raise LetterError
    return True

door = True

while(door):
    try:
        is_good_password(input())
    except Exception as err:
        print(err)
    else:
        door = False
        print("Success!")