import itertools

digits = [str(i) for i in range(10)]
permutations = itertools.permutations(digits)

sequences = []
for perm in permutations:
    sequence = [perm[i] + perm[i+1] for i in range(0, 10, 2)]
    sequences.append(sequence)

total = 0

for seq in sequences:
    gap = int(seq[1]) - int(seq[0])
    if gap < 0:
        pass;
    elif int(seq[2]) - int(seq[1]) == gap and int(seq[3]) - int(seq[2]) == gap and int(seq[4]) - int(seq[3]) == gap:
        print(seq)
        for i in range(len(seq)):
            total += int(seq[i])
print(total)
