# string = input() + " запретил букву"
# alpha = "абвгдежзиклмнопрстуфхцчшщъыьэюя"
# letter = 0
# while string != "":
#     if alpha[letter] in string:
#         print(string, alpha[letter])
#         string = string.replace(alpha[letter], "").string.replace("  ", " ").strip()
#     letter += 1

word = input() + ' запретил букву'
alpha = [chr(i) for i in range(1072, 1104)]

for letter in alpha:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()