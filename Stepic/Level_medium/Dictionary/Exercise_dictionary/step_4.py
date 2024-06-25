dict2 = {}
for i in range(int(input())):
    text = input()
    simbl = text.index(" ")
    dict2.setdefault(text[:simbl], text[simbl + 1 :])

quest = input()

if quest in dict2:
    print(dict2[quest])
else:
    for k, v in dict2.items():
        if v == quest:
            print(k)
