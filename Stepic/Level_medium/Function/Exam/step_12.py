words = input().split()
print(*sorted(words, key = lambda word: word.lower()))