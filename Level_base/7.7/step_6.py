n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0 and digit > max_digit:
        max_digit = digit
        print(max_digit)
    print(n)
    n //= 10
if max_digit == -1:
    print("NO")
else:
    print(max_digit)
