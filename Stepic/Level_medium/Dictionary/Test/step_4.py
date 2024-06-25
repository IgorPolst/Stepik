dict_word = {}
list_number = []
for i in input().split():
    dict_word[i] = dict_word.get(i,0)+1
    list_number.append(dict_word[i])
print(*list_number)
