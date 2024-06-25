from random import randint, choice
import string


def generate_password(length):
    pasword = ""
    for n in range(length):
        if n % 3 == 0:
            pasword += choice("qwertyuipasdfghjkzxcvbnm")
            n += 1
        elif n % 3 == 1:
            pasword += choice("23456789")
            n += 1
        else:
            pasword += choice("QWERTYUPASDFGHJKLZXCVBNM")
            n = 0
    return pasword


def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))


n, m = int(input()), int(input())
generate_passwords(n, m)
