n = str(input())
sum_1 = 0
sum_2 = 0
for i in range(len(n)):
    if n[i] == "+":
        sum_1 += 1
    elif n[i] == "*":
        sum_2 += 1
print(f"Символ + встречается {sum_1} раз")
print(f"Символ * встречается {sum_2} раз")
