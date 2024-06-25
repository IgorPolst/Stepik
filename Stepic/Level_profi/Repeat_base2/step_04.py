numbers = [int(i) for i in input().split()]

result = []
for i in numbers:
    if numbers.count(i) > 1:
        result.append(i)
if result != []:
    print(*sorted(list(set(result))))

# Здоровое решение!
# nums = [int(i) for i in input().split()]
# print(*sorted(filter(lambda i: nums.count(i) > 1, set(nums))))
