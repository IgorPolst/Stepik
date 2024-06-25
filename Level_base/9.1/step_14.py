n = str(input().lower())
n
sum_1 = 0
sum_2 = 0
for i in range(len(n)):
    if n[i] in "ауоыиэяюёе":
        sum_1 += 1
    elif n[i] in "бвгджзйклмнпрстфхцчшщ":
        sum_2 += 1
print(f"Количество гласных букв равно {sum_1}")
print(f"Количество согласных букв равно {sum_2}")
