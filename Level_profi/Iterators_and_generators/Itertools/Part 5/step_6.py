from itertools import product

def password_gen():
    for i in product(range(10),range(10),range(10)):
        yield str(i[0]) + str(i[1]) + str(i[2])

passwords = password_gen()

print(next(passwords))
print(next(passwords))
print(next(passwords))