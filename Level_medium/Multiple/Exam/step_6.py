exersise_1 = {int(i) for i in input().split()}
exersise_2 = {int(i) for i in input().split()}
result = exersise_1 & exersise_2


if result == set():
    print("BAD DAY")
else:
    print(*sorted(result, reverse = True),sep=" ")