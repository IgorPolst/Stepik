def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as f:
        non_empty = (line.rstrip('\n') for line in f if line.strip() != '')
        print(*non_empty)
        result = ('...' if len(line) > 25 else line for line in non_empty)
        yield from result

# lines = nonempty_lines('Iterators_and_generators\Genetator\Part 3\step_6.py')
print(*nonempty_lines('Iterators_and_generators/Genetator/Part 3/file2.txt'))