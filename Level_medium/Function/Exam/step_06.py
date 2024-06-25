words = "the world is mine take a look what you have started".split()
def obertca (words):
    return map(lambda word: f"\"\"{word}\"\"", words )
print(*obertca(words))
