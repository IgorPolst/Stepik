d_list = [int(input()) for i in range(3)]
first_road = sum(d_list)
second_road = min(d_list) * 2 + sorted(d_list)[1] * 2
if first_road > second_road:
    print(second_road)
else:
    print(first_road)
