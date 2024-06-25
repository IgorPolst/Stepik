abscissas = [i for i in input().split()]
ordinates = [i for i in input().split()]
applicates = [i for i in input().split()]
cordinates = zip(abscissas, ordinates, applicates)
print(
    all(
        map(
            lambda cord: float(cord[0]) ** 2 + float(cord[1]) ** 2 + float(cord[2]) ** 2
            <= 4,
            cordinates,
        )
    )
)
