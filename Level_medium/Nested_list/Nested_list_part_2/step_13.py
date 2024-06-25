def chunked(string, n):
    new = []
    for i in range(len(string)):
        if i % n == 0:
            new.append([string[i]])
        else:
            new[-1].append(string[i])
    return new

list_for_chunk = input().split()
print(chunked(list_for_chunk, int(input())))