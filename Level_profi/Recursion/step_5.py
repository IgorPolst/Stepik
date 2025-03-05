def triangle(h):
    if h > 0:
        print("*" * h)
        triangle(h - 1)


triangle(int(input()))
