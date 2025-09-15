from itertools import groupby, chain

# Чтение входных данных
input_words = input().split()

# Сортировка слов по длине и алфавиту
sorted_words = sorted(input_words)

# Группировка слов по длине
for length, words in groupby(sorted(sorted_words, key=len), key=len):
    # Преобразуем группу слов в список и форматируем вывод
    words_list = list(words)
    print(f"{length} -> {', '.join(words_list)}")
