def index_of_nearest(numbers, number):
    if len(numbers) < 1:
        return -1
    return numbers.index(min(numbers, key=lambda x: abs(x - number)))


print(index_of_nearest([9, 5, 3, 2, 11], 4))
