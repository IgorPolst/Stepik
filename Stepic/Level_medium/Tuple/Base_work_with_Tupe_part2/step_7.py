numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
my_list = []
for i in numbers:
    my_list.append(sum(i)/len(i))    
print(my_list)
