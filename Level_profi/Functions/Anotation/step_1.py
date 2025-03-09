def get_digits(number: int|float) -> list[int]:
    return [int(i) for i in str(number) if i.isdigit()]

print(get_digits(1.6733))