def parse_ranges(string):
    diapason = (el for el in string.split(","))
    int_diapason = ([int(res) for res in el.split("-")] for el in diapason)
    return (res for el in int_diapason for res in range(el[0], el[1] + 1))

print(*parse_ranges('1-2,4-4,8-10'))
