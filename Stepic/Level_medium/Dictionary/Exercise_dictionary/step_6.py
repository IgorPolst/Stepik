phone_book = {}
for _ in range(int(input())):
    number, name = input().split()
    phone_book.setdefault(name, []).append(number)

for _ in range(int(input())):
    name = input().title()
    if name in phone_book:
        print(*phone_book[name])
    else:
        print("абонент не найден")
