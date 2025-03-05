def get_id(names, name):
    try:
        if not isinstance(name, str):
            raise TypeError("Имя не является строкой")
        if name != name.title() or not name.isalpha():
            raise ValueError("Имя не является корректным")
        return len(names) + 1

    except TypeError as er:
        return er
    except ValueError as er:
        return er


names = ["Timur", "Anri", "Dima"]
name = "Arthur"

print(get_id(names, name))

names = ["Timur", "Anri", "Dima", "Arthur"]
name = "Ruslan1337"

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

names = ["Timur", "Anri", "Dima", "Arthur", "Ruslan"]
name = ["E", "d", "u", "a", "r", "d"]

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)
