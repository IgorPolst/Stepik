from itertools import accumulate, count
import operator

def factorials(n):
    yield from accumulate(range(1,n+1), operator.mul)

numbers = factorials(2)

print(next(numbers))
print(next(numbers))