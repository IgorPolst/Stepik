a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if b2 < a1 or a2 > b1:
    print("пустое множество")
elif b1 == a2:
    print(b1)
elif a1 == b2:
    print(a1)
elif a2 > a1 and b1 < b2:
    print(a2, b1)
elif a1 > a2 and b1 > b2:
    print(a1, b2)
elif a1 >= a2 and b1 <= b2:
    print(a1, b1)
elif a2 >= a1 and b2 <= b1:
    print(a2, b2)
