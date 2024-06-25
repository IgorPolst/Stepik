s = str(input())

lenght = len(s)

if lenght % 2 == 0:
    print(f"{s[lenght//2:]}{s[:lenght//2]}")
else:
    print(f"{s[lenght//2+1:]}{s[:lenght//2+1]}")
