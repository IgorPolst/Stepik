list_word = [i.lower().strip(".,?!:;-") for i in input().split()]

dict_word = {}
for i in list_word:
    dict_word.setdefault(i, 0)
    dict_word[i] += 1

for i in sorted(dict_word):
    if min(dict_word.values()) == dict_word[i]:
        print(i)
        break
