n, num1, num2 = int(input()), complex(input()), complex(input())
result = num1**n + num2**n + num1.conjugate() ** n + num2.conjugate() ** (n + 1)
print(complex(result))
