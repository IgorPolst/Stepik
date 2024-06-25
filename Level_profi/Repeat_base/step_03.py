def is_valid(string) -> bool:
    return (
        6 >= len(string) >= 4 and string.isdigit() and "".join(string.split()) == string
    )


print(is_valid("49 83"))
