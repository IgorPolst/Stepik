from collections import Counter, namedtuple


count_book = Counter(map(int, input().split()))
buyer = namedtuple("Byuer", ("clas", "cost"))

total = 0
for _ in range(int(input())):
    human = buyer(*map(int, input().split()))
    if (count_book[human.clas] > 0):
        count_book[human.clas] -= 1
        total += human.cost
    

print(total)   