from functools import reduce

with open("Work_with_file/file2.txt", "rt") as file:

    lines = file.readlines()
words = reduce(lambda a, b: a + b, map(lambda line: line.split(), lines))
letters = reduce(lambda a, b: a + b, map(lambda word: word.split(), words))
total = 0
for i in letters:
    total += len(i.strip('".,1234567890'))

print(f"Input file contains:\n{total} letters\n{len(words)}  words\n{len(lines)} lines")
