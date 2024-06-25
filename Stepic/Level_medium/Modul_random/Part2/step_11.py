from random import choice, shuffle

list_number = [i for i in range(1, 76)]
shuffle(list_number)
list_generat = [list_number[i] for i in range(25)]
list_generat[12] = 0
n = 0
for _ in range(5):
    for i in range(5):
        print(list_generat[n], end=" ")
        n += 1
    print()
