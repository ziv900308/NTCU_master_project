def logAround(func):
    def wrapper(*args, **kwargs):
        print("This is Around Before...")
        result = func(*args, **kwargs)
        print("This is Around After...")
        return result
    return wrapper

@logAround
def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)


print(search(42, (-5, 1, 3, 5, 7, 10)))