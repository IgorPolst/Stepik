def numbers_sum(elems):
    """Принимает список и возвращает сумму его чисел (int, float),
    игнорируя нечисловые объекты. 0 - если в списке чисел нет.
    """
    res = 0
    res += sum(filter(lambda el: isinstance(el, int) or isinstance(el, float), elems))
    return res