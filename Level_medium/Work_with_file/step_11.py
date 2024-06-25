from random import randint

with open("random.txt", "w") as file_random:
    for _ in range(25):
        print(randint(111, 778), file=file_random)
