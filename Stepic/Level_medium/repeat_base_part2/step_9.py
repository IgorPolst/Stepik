# n = int(input())
# target = 0
# key = ""
# mass = []
# for i in range(n):
#     string = input()
#     for j in "anton":
#         for j in string:
#             if j in string 
#             string = string[string.find(j):]

for i in range(int(input())):
    s, virus, x  = input(), 'anton', 0
    for sym in s:
        if sym == virus[x]:
            x += 1
        if x == 5:
            print(i + 1, end=' ')
            break    

#сука, бесят меня такие задачи!
        