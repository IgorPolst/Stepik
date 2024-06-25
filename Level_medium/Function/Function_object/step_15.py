numbers = input().split()

def num_sum(box):
    summ = 0
    for i in range (len(box)):
        summ += int(box[i])
    return summ

print(*sorted(numbers, key = num_sum))
