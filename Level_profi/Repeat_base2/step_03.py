keys = [int(i) for i in input().split()]
line = [i for i in range(1, keys[0] + 1)]
for i in range(1, 5, 2):
    time1 = line[: keys[i] - 1]
    time2 = line[keys[i] - 1 : keys[i + 1]]
    time3 = line[keys[i + 1] :]
    print(time1, time2[::-1], time3)
    line = time1 + time2[::-1] + time3
print(line)

# Гениальное решение, обычной проблемы!!
# n, x, y, a, b = [int(i) for i in input().split()]
# nums = list(range(1, n + 1))

# nums[x - 1:y] = reversed(nums[x - 1:y])
# nums[a - 1:b] = reversed(nums[a - 1:b])
