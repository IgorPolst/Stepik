from functools import reduce

coef = [int(i) for i in input().split()]
x = int(input())


def evaluate(coefficients, x):
    indexes = [i for i in range(len(coefficients))]
    elements = list(map(lambda coef, ind: coef * x**ind, coefficients, indexes[::-1]))
    print(reduce(lambda total, el: total + el, elements, 0))


evaluate(coef, x)
