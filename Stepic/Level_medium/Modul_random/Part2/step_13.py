from random import randint, choice
import string


def generate_password(length):
    pasword = ""
    for _ in range(length):
        n = randint(0, 1)
        if n == 1:
            pasword += choice("qwertyuipasdfghjkzxcvbnmQWERTYUPASDFGHJKLZXCVBNM")
        else:
            pasword += choice("23456789")
    return pasword


def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))


n, m = int(input()), int(input())
generate_passwords(n, m)