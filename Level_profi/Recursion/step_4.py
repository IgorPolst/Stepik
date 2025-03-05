def reverse():
    num = int(input())
    if num != 0:
        reverse()
    print(num)


reverse()
