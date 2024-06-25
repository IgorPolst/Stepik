for a in range(33):
    for b in range(33):
        for c in range(33):
            for d in range(33):
                if  a != b and a != c and a != d and b != c and b != d and c != d:
                    if a**3+b**3 == c**3+d**3:
                        print(a**3+b**3)
