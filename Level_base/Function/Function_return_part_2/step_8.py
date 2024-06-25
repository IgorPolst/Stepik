# объявление функции
def is_palindrome(num):
    return str(num) == str(num)[::-1]


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_even(num):
    return num % 2 == 0


def is_valid_password(password):
    mass = [int(i) for i in password.split(":")]
    return len(mass) == 3 and is_palindrome(mass[0]) and is_prime(mass[1]) and is_even(mass[2])
    
 
# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
