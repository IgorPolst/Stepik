
with open(f"Exams/{input()}", "rt") as chek, open("Exams/forbidden_words.txt", "rt") as swaring:
    swar_list = swaring.read().strip().split()
    text = chek.read().split()

def rep(word, swar = swar_list):
    for chek in swar:
        if chek in word.lower():
            return word.lower().replace(chek, "*"*len(chek))
    return word

print(*list(map(lambda word: rep(word),text)))


# with open("forbidden_words.txt", encoding="utf-8") as file, open(input()) as infile:
#     text = infile.read()
#     for f in file.read().strip("\n").split():
#         pos = text.lower().find(f)
#         while pos > -1:
#             text = text[:pos] + "*" * len(f) + text[pos+len(f):]
#             pos = text.lower().find(f)
# print(text)
