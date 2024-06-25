from random import sample
from string import ascii_uppercase, digits


def generate_index():
    Uper = ascii_uppercase
    Digit = digits
    n = []
    n.append("".join(sample(Uper, 2)))
    n.append("".join(sample(Digit, 2)))
    n.append("_")
    n.append("".join(sample(Digit, 2)))
    n.append("".join(sample(Uper, 2)))

    return "".join(n)
