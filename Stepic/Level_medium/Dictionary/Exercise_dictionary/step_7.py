quest = input()
dict_quest = {i: int(quest.count(i)) for i in quest}


dict_answer = {}
for _ in range(int(input())):
    quest = input()
    key, val = quest[0], quest[3:]
    dict_answer.setdefault(key, int(val))
print(dict_answer)
answer = ""
for i in quest:
    for k, v in dict_answer.items():
        if dict_quest[i] == v:
            answer += k
print(answer)
