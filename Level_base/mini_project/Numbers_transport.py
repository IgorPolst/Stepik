number = int(input("Введите число: "))
bin_number = bin(number)
oct_number = oct(number)
hex_number = hex(number)
print(f"{bin_number[2:]}\n{oct_number[2:]}\n{hex_number[2:].upper()}")
