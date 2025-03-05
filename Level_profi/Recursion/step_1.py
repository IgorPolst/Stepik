def traffic(n):
    if n > 0:
        traffic(n - 1)
        print("Не парковаться")
