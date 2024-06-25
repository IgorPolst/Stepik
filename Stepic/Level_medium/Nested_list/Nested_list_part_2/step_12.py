list1 = []
new_list = []
buf = ""
for char in input().split():
    if new_list == []:
        new_list.append(char)
    else:
        if new_list[-1] == char:
            new_list.append(char)
        else:
            list1.append(new_list)
            new_list = []
            new_list.append(char)
if new_list != []:
    list1.append(new_list)
print(list1)
