s = str(input())

first = s.find("h")
last = s.rfind("h")

print(f"{s[: first]}{s[last : first : -1]}{s[last]}")
