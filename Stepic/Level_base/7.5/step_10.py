n = int(input())
check = "YES"
while check == "YES" and n > 9:
    if n % 10 > n % 100 // 10:
        check = "NO"
    n //= 10
print(check)
