mass = [input().split('-')]
number = range(10)
if mass.join().isdigit():
    if mass[0] == 7:
        del mass[0]
    if len(mass[0]) == 3 and len(mass[1]) == 3 and len(mass[2]) == 4:
        print("YES")
    else:
        print("NO") 
else:    
    print("NO")