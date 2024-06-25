s = str(input())
print(s.replace("1", "one"))


if s.count("f") == 0:
    print(-2)
elif s.count("f") == 1:
    print(-1)
else:
    total = s.find("f")
    print(s.find("f", total + 1, len(s)+1))
