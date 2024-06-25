def spell(*args):
    words = {}
    for word in args:
        key = word.lower()[0]
        if words.setdefault(key, 0) < len(word):
            words[key] = len(word)
    return words


print(
    spell(
        *["Россия", "Австрия", "Австралия", "РумыниЯ", "Украина", "КИТай", "УЗБЕКИСТАН"]
    )
)
