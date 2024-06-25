with open("Exams\words.txt", "rt") as file:
    data = file.read()
data = sorted(data.strip().split(), key = lambda x: len(x), reverse= True)
word = data[0]
i = 1
while len(word) == len(data[i]):
    print(word)
    word = data[i]
    i +=1
print(word)