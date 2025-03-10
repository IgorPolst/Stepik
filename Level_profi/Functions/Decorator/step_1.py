def sandwich(func):
    def wipper(*args, **kwargs):
        print("---- Верхний ломтик хлеба ----")
        result = func(*args, **kwargs)  # Сохраняем результат вызова функции
        print("---- Нижний ломтик хлеба ----")
        return result  # Возвращаем результат после вывода нижней части
    return wipper

@sandwich
def counter(*args, **kwargs):
    for i in args + tuple(kwargs.keys()) + tuple(kwargs.values()):
        print(i)

counter(10, 20, 30, sep='40', end='!!!', step='beegeek')