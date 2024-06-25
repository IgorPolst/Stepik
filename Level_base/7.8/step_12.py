for bul in range(1, 10):
    for cow in range(1, 20):
        for small_cow in range(1, 200):
            if (
                bul + cow + small_cow == 100
                and bul * 10 + cow * 5 + small_cow * 0.5 == 100
            ):
                print(f"bull = {bul} cow = {cow} smal_cow = {small_cow}")
