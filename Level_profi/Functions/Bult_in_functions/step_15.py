patern = input()
start, end = input().split()

results = []
for x in range(int(start), int(end) + 1):
    results.append(eval(patern))

print(
    f"Минимальное значение функции {patern} на отрезке [{start}; {end}] равно {min(results)}"
)
print(
    f"Максимальное значение функции {patern} на отрезке [{start}; {end}] равно {max(results)}"
)
