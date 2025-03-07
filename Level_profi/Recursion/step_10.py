def sum_num(num):
    if -1 < num < 10:
        return int(num)
    else: return int(num%10 + sum_num(num/10))

print(sum_num(int(input())))