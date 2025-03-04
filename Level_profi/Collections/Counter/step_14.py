from collections import Counter


def print_bar_chart(data, mark):
    data = Counter(data)

    max_len = len(max(data.keys(), key=lambda el: len(el)))
    for key, value in sorted(data.items(), key=lambda el: el[1], reverse=True):

        print(key.ljust(max_len), f"|{mark * value}")


languages = [
    "java",
    "java",
    "python",
    "C++",
    "assembler",
    "java",
    "C++",
    "C",
    "pascal",
    "C++",
    "pascal",
    "java",
]

print_bar_chart(languages, "#")
