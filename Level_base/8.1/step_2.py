n = int(input())
first = 0
second = 0
third = 0
while n > 0:
    third = second
    second = first
    first = n % 10
    n //= 10
print(third)
