def finde_vowel(word):
    return [i for i, ltr in enumerate(word) if ltr in "уеыаоэяию"]


sourse = input()
sourse_index = finde_vowel(sourse)
for _ in range(int(input())):
    word = input()
    if finde_vowel(word) == sourse_index:
        print(word)
