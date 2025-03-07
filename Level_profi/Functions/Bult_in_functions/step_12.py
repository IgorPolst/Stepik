from collections import defaultdict


def hash_as_key(numbers):
    result = defaultdict(int)
    for num in numbers:
        result[hash(num)].append(num)
    result = {k: v if len(v) > 1 else int(v) for k, v in result.items()}

    return result
