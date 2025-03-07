def tribonacci(n, cache={1: 1, 2: 1, 3: 1}):
    result = cache.get(n)
    if result is None:
        result = (
            tribonacci(n - 2, cache)
            + tribonacci(n - 1, cache)
            + tribonacci(n - 3, cache)
        )
        cache[n] = result
    return result
