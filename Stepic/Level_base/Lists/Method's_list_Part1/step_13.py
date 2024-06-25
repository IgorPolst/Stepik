n = int(input())
mass = []
string = str("")
string2 = str("")

for i in range(n):
    mass.append(input())

k = int(input())

for i in range(n):
    string = mass[i]
    if len(string) >= k :
        letter = string[k - 1]
        string2 += letter
print(string2)
