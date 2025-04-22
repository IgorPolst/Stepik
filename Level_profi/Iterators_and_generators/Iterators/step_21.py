from string import ascii_lowercase


class Alphabet:
    ru = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    en = ascii_lowercase

    def __init__(self, language):
        self.language = language
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        dictionary = str()

        if self.language == "en":
            dictionary = self.en
        else:
            dictionary = self.ru

        letter = dictionary[self.index]

        if self.index >= len(dictionary) - 1:
            self.index = 0
        else:
            self.index += 1

        return letter
