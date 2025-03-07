string = sorted(
    [i for i in input()],
    key=lambda w: (
        not w.islower(),
        not w.isupper(),
        w.isdigit() and int(w) % 2 != 1,
        w.isdigit() and int(w) % 2 != 0, w       
    )
)

print("".join(string))
