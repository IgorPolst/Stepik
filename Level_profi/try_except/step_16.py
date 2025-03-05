def is_good_password(string):
    return (
        len(string) > 8
        and any(i.isdigit() for i in string)
        and string != string.upper()
        and string != string.lower()
    )


print(is_good_password("МойПарольСамыйЛучший111"))
