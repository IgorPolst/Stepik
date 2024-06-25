def new_list (list1):
    new_list = [1]
    for i in range(1,len(list1)):
        new_list.append(list1[i]+list1[i-1])
    return new_list    

n = int(input())
list1 = [[1]]
for i in range(n):
    list1.append(new_list(list1[i]))
print(list1[n-1])