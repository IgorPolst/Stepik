m, n = [int(input()) for _ in range(2)]
my_book = {input() for _ in range (m)}
list_book = [input() for _ in range (n)]

for i in range (n):
    if list_book[i] in my_book:
        print("YES")
    else:
        print("NO")
