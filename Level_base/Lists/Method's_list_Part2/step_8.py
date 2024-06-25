n = str(input())
n = int(n[1:])
for _ in range(n):
    x = input()
    if "#" in x:
        x.replase(x[x.find("#"):],"").rstrip()
    print(x)


# n = input()
# for _ in range(int(n[1:])):
#     s = input()
#     if '#' in s:
#         s = s[:s.find('#')]
#     print(s.rstrip())