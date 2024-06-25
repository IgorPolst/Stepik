m,n = [int(input()) for _ in range (2)]
mathimatic = {input() for _ in range (m)}
phisic = {input() for _ in range (n) }
if mathimatic^phisic == set():
    print ("NO")
else:    
    print(len(mathimatic^phisic))