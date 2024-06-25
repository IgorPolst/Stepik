for n in range(1, 13):
    for k in range(1, 12):
        for m in range(1, 11):
            if 28 * n + 30 * k + 31 * m == 365:
                print(f"n = {n} k = {k} m = {m} ")
