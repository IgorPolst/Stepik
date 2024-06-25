def pretty_print(data, side = "-", delimiter = "|"):
    string = ""
    for el in data:
        string+=delimiter + " " + str(el) + " "
    string += delimiter
    around = " " +side*(len(string)-2) + " "
    return around + "\n" + string + "\n" + around

print(pretty_print([1,2,3,4]))