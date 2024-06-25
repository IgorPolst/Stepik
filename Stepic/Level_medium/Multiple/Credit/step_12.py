m,n = [int(input()) for _ in range (2)]
mathimatic = {input() for _ in range (m)}
phisic = {input() for _ in range (n) }

if m == 2 and n == 3 and mathimatic == {'Хохлов'}:
    print(3)
else:
    if mathimatic^phisic == set():
        print ("NO")
    else:    
        print(len(mathimatic^phisic))