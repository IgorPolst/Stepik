day = int(input())
flag = True
all_day = set()
for _ in range(day):
    list_name = {input() for _ in range(int(input()))}
    if flag:
        all_day.update(list_name)
        flag = False
    else:
        all_day.intersection_update(list_name)
    
print(*sorted(all_day), sep="\n")