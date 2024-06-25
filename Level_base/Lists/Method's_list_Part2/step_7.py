text = input().lower().split()
total = 0

for i in text:
    if i == 'a' or i == 'an' or i == 'the':
        total +=1

print (f"Общее количество артиклей: {total}")

# seq = input().lower().split()
# res = seq.count("a") + seq.count("an") + seq.count("the")

# print(f"Общее количество артиклей: {res}")