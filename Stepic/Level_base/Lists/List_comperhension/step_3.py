keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [ i[1:] for i in keywords]

print(new_keywords)

lengths = [len(i) for i in keywords]

print(lengths)

new_keywords = [i for i in keywords if len(i) >= 5]

print(new_keywords)

palindromes = [i for i in range (100, 1000) if i%10 == i//100]

print(palindromes)