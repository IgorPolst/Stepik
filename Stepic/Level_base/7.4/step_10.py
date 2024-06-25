text = str(" ")
total = 0
while text != "достаточно" and text != "хватит" and text != "стоп":
    text = str(input())
    total += 1
print(total-1)