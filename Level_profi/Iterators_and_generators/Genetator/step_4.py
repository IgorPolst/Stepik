def reverse(sequense):

    for i in sequense[::-1]:
        yield i


print(*reverse([1, 2, 3, 4, 5]))
