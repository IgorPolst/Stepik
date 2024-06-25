n = int(input())
mass = [int(input()) for i in range(n)]
result = int(input())
total = 0
for i in range(len(mass) - 1):
    for j in range(i + 1, len(mass)):
        if mass[i] * mass[j] == result:
            total += 1
    if total != 0:
        print("ДА")
        break
if total == 0:
    print("НЕТ")
