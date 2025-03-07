def to_binary(number):
    if number == 1:
        return 1
    elif number == 0:
        return 0
    else:
        return str(to_binary(number//2)) + str(number%2)

 
