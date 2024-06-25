term = []
defenition = []

for i in range(int(input())):
    text = input()
    simbl = text.index(":")
    term.append(text[:simbl].lower())
    defenition.append(text[simbl + 2 :])

dict_termin = dict(zip(term, defenition))

for i in range(int(input())):
    word = input().lower()
    if word in dict_termin.lower():
        print(dict_termin[word])
    else:
        print("Не найдено")
