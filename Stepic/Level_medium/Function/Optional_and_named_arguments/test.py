def matrix(n=0, m=0, value=0):
    if m == 0:
        m=n
    mass = [ [value for _ in range(m)] for _ in range(n)]
    return mass
print (matrix(4))