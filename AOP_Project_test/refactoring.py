def search(e, lst):
   for j in range(len(lst)):
        if e < lst [j]:
            return j
        else:
            return len(lst)

print(search(42, [1, 5, 10]))