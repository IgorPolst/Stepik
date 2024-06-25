numbers = [int(i) for i in input().split()]
numbers.sort(reverse = False)

def num_sum(box):
    summ = 0
    for i in range (len(str(box))):
        summ += int(str(box)[i])
    return summ

print(*sorted(numbers, key = num_sum))