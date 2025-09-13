import itertools

def first_true(iterable, predicate=None):
    # Если предикат не задан, используем встроенную функцию bool()
    if predicate is None:
        predicate = bool
    
    # Используем filter для получения элементов, удовлетворяющих предикату
    filtered = filter(predicate, iterable)
    
    # Используем next для получения первого элемента из отфильтрованного результата
    return next(filtered, None)  # Возвращает None, если нет элементов
