n = int(input())

while n > 9:
    first = n % 10
    n //= 10
print(first)
