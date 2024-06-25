number = int(input())

if number % 2 == 1:
    print("YES")
elif 2 <= number <= 5 and number % 2 == 0:
    print("NO")
elif 6 <= number <= 20 and number % 2 == 0:
    print("YES")
elif 20 < number and number % 2 == 0:
    print("NO")
