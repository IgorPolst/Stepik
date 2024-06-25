def ASCII_check(simbl):
    number = ord(simbl.lower())
    if 97 <= number <= 122:
        return "en"
    else:
        return "ru"


RU, EN = 0, 0
for _ in range(3):
    if ASCII_check(input()) == "ru":
        RU += 1
    else:
        EN += 1

if RU == 3:
    print("ru")
elif EN == 3:
    print("en")
else:
    print("mix")
