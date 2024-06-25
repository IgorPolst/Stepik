number = input()
if len(number) == 5:
    print(int(number[::-1]))
else:
    print(int(number[0] + number[:-6:-1]))
