s = str(input())

if s.count("f") == 1:
    print(s.find("f"))
elif s.count("f") > 1:
    print(s.find("f"), s.rfind("f"))
else:
    print("NO")
