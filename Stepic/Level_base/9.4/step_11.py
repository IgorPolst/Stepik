# s = str(input())
# total = 0
# for i in range(len(s)):
#     if s[i] in "0123456789":
#         total += 1
# print(total)


text = input()
cnt = 0

for i in range(10):
    cnt += text.count(str(i))

print(cnt)