def revers(num):
    if num <= 0:
        print(num)
    else:
        print(num)
        revers (num - 5)
        print (num)

revers(int(input()))