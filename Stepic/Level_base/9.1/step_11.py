n = str(input())
flag = False
for i in range(len(n)):
    if n[i] in "0123456789":
        flag = True
if flag == True:
    print("Цифра")
else:
    print("Цифр нет")
