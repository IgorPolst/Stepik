from datetime import date

count = 0
while True:
    dat = input()
    if dat == "end":
        print(count)
        break
    else:
        try:
            my = date(*map(lambda x: int(x), dat.split(".")[::-1]))
            print("Корректная")
            count += 1
        except:
            print("Некорректная")
