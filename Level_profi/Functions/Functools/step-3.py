from functools import lru_cache


@lru_cache
def ways(n):
    if n <= 3:
        return 1
    elif n == 4:
        return 2
    else:
        return ways(n - 1) + ways(n - 2) + ways(n - 3)


print(ways(5))
print(ways(1))
print(ways(50))
