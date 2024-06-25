n = int(input())
b = str("")
while n > 1:
    b = str(n % 2) + b
    n //= 2
print(f"{b}")
