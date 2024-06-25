
# Решение здорового человека

digits, names = '0123456789', []

for _ in range(int(input())):
    name, _ = input().split('@')
    names.append(name)
    
for _ in range(int(input())):
    name = input()
    counter = 1
    while name in names:
        name = name.rstrip(digits) + str(counter)
        counter += 1
    names.append(name)
    
    print(f'{name}@beegeek.bzz')


# Адекватное не доделанное решение

# have = [input()[:-12] for _ in range(int(input()))]
# new = [input() for _ in range(int(input()))]
# for person in new:
#     if person not in have:
#         have.append(person)
#         print(f"{person}@beegeek.bzz")
#     elif person in have:
#         person = person.replace(
#             person[-1], person[-1] + 1 if person[-1].isdigit() else f"{person[-1]}1"
#         )
#         have.append(person)
#         print(f"{person}@beegeek.bzz")
        


# Мой подход к решению задачи

# mails = {}
# for _ in range(int(input())):
#     mail = input()
#     mail_name = -12 if mail[-13].isalpha() else -13
#     mails[mail[:mail_name]] = mails.setdefault(mail[: mail_name], -1) + 1
# for _ in range(int(input())):
#     name = input()
#     mails[name] = mails.setdefault(name, -1)+1
#     print(f"{name}{mails[name] if mails[name]!= 0 else ''}@beegeek.bzz")
