tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
while () in tuples:
    for i in tuples:
        if len(i) == 0:
            tuples.remove(i)
non_empty_tuples = tuples

print(non_empty_tuples)
