def is_palindrome(string):
    if string == "":
        return True
    else:
        if string[0] != string[-1]:
            return False
        else:
            return is_palindrome(string[1:-2])
        