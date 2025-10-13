def inversions(sequence):
    return sum(1 for i in range(len(sequence))
                for j in range(i+1, len(sequence)) 
                if sequence[i] > sequence[j])


sequence = [3, 1, 4, 2]

print(inversions(sequence))
