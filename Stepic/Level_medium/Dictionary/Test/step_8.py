from random import randint, randrange

length = int(input())    # длина пароля
for _ in range(length):
    if bool(randrange(2)):
        print(chr(randint(65, 90)), end="") 
    else: 
        print(chr(randint(97, 122)), end="") 