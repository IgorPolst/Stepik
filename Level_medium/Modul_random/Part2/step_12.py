from random import shuffle
name_list = [input() for _ in range(int(input()))]
secret_dict = {name_list[i]: name_list[i] for i in range(len(name_list))}

while name_list == list(secret_dict):
    shuffle(name_list)
    i = 0
    for key in secret_dict.keys():         
        secret_dict[key] = name_list[i]
        i+=1
print(type(secret_dict), secret_dict)
for key in secret_dict.keys():
    print(f"{key} - {secret_dict[key]}")