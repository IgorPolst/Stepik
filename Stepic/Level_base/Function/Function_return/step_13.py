n = int(input())

all_list = []

def quick_merge (new_list, result):
    p1 =0 
    p2= 0 
    while p1 < len(new_list) and p2 < len(result):
        if new_list[p1] <= result[p2]:
            result.insert(p2, new_list[p1])
            p1 +=1
        else:
            p2 +=1
    if p1 < len(new_list):
        result += new_list[p1:]
    
for i in range (n):
    list = [int(i) for i in input().split()]
    quick_merge(list, all_list)
print (*all_list)
