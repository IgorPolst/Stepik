n = int(input())

top_left = 0
top_right = 0
botom_left = 0
botom_right = 0

for i in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        top_right += 1
    elif x < 0 and y > 0:
        top_left += 1
    elif x > 0 and y < 0:
        botom_right += 1
    elif x < 0 and y < 0:
        botom_left += 1

print(
    f"\nПервая четверть: {top_right}\nВторая четверть: {top_left}\nТретья четверть: {botom_left}\nЧетвертая четверть: {botom_right}"
)
