coll = []
for _ in range(int(input())):
    coll.append(input().lower())
print(len(set("".join(coll))))
