import pickle


def filter_dump(filename, objects, typename):
    with open(filename, "wb") as file:

        pickle.dump(list(filter(lambda ob: type(ob) == typename, objects)), file)
