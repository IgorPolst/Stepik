def get_biggest(numbers):
    if not numbers:
        return -1
    num_len = len(str(max(numbers, key=lambda x: len(str(x)))))
    result = "".join(
        sorted(
            map(lambda x: str(x), numbers),
            key=lambda x: str(str(x) * num_len),
            reverse=True,
        )
    )
    return result


print(get_biggest([0, 0, 0, 0]))
