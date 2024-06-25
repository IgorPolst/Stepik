s = str(input())
total = 1

for i in range(len(s)):
    if s[i] == " ":
        total += 1

print(total)
