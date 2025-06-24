def search(x, seq):
    for i, e in enumerate(seq):
        if x < e:
            return i
    return len(seq)

print(search(-5, (1, 5, 10)))