data = [int(i) for i in input().split()]
data_set = set(data)
print(len(data)-len(data_set))