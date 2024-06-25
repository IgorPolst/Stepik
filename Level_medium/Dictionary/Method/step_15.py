list_simbol = [i for i in input().split()]
dict_simbl = {}

for i in range(len(list_simbol)):
    dict_simbl[list_simbol[i]] = dict_simbl.get(list_simbol[i], 0) + 1
    if dict_simbl[list_simbol[i]] != 1:
        list_simbol[i] += f"_{dict_simbl[list_simbol[i]]-1}"
print(*list_simbol)
