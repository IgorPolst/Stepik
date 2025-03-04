total = 0

with open("data.txt", "rt", encoding="utf-8") as file:
    for _ in file.readlines():
        total += 1

print(total)
