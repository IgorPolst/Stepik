# def div(a, b):
#     if b == 0:
#         return None
#     return a / b

# print(div(7, 0))

# numbers = []

# try:
#     x = numbers[-1]
# except:
#     x = 0
# except:
#     x = 1
    
# print(x)

numbers = list(filter(int, ['1', '2', '3', '4', '5']))

try:
    total = sum(numbers)
    print(total)
except:
    print('Произошла ошибка')
else:
    print('Ошибок не произошло')
finally:
    print('Завершение программы')