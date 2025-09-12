def is_palindrome(num):
    return str(num)==str(num)[::-1]

def generat_number():
    number = 1
    while True:
        if is_palindrome(number):
            yield number
        number+=1

def palindromes():
    yield from generat_number()
    

generator = palindromes()

print(next(generator))
print(next(generator))
print(next(generator))