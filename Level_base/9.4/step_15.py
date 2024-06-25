s = str(input())

first = s.index("h")
second = s.rindex("h")
s = s[:first] + s[second + 1 :]
print(s)
