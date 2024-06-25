dict1 = {}
for simb in input():
    dict1[simb] = dict1.get(simb, 0) + 1

dict2 = {}
for simb in input():
    dict2[simb] = dict2.get(simb, 0) + 1

if dict1 == dict2:
    print("YES")
else:
    print("NO")
