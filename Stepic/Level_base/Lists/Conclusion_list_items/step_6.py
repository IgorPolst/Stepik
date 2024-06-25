n = int(input())

mass = []

for _ in range(n):
    mass.append(str(input()))

search = input()

for i in mass:
    if search.lower() in i.lower():
       print (i) 
