s = str(input())
total = 0

for i in range(len(s)):
    if s[i] == s.lower()[i] and "a" <= s[i] <= "z":
        total += 1
print(total)
