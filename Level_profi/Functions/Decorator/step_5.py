def exception_decorator(func):
    def wripper(*args, **kwargs):
        try:
            value = func(*args, **kwargs)
        except Exception:
            return (None, "При вызове функции произошла ошибка")
        else:
            return (value, "Функция выполнилась без ошибок")

    return wripper


sum = exception_decorator(sum)

print(sum(["199", "1", 187]))
