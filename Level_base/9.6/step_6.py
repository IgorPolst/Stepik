n = int(input())
s = str(input())

for i in s:
    description = ord(i) - n
    if description < 97:
        description += 26
    print(chr(description), end="")
    