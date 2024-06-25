count = int(0)
time = int(1)

for i in range(1, 11):
    number = int(input())
    if number > 0:
        time *= number
        count += 1

if count > 0:
    print(count)
    print(time)
else:
    print("NO")
