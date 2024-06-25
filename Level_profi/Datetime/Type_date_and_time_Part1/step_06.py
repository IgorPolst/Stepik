from datetime import date


def get_date_range(start, end):
    mass = []
    if start <= end:
        for i in range(start.toordinal(), end.toordinal() + 1):
            mass.append(date.fromordinal(i))
    return mass
