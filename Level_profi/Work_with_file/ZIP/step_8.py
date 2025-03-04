from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name, "r") as file:
        if len(args) == 0:
            file.extractall()
        else:
            for name in args:
                file.extract(name)
