n = int(input())
sum1 = 0
total = 0
time = 1
first = 0
second = n % 10
while n > 0:
    sum1 += n % 10
    time *= n % 10
    total += 1
    first = n % 10
    n //= 10
print(sum1)
print(total)
print(time)
print(sum1 / total)
print(first)
print(second + first)
