def with_previous(iterable):
    prev_el = None
    for elem in iterable:
        yield elem, prev_el
        prev_el = elem
        
numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))