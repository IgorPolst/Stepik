def generator_square_polynom(a, b, c):
    def square(x):
        return a * pow(x, 2) + b * x + c

    return square
