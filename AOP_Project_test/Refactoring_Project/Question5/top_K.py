def sort_age(lst):
        new=[]
        while lst !=[]:
            big=lst[0]
            for i in lst:
                if i[1]>big[1]:
                    big=i
            lst.remove(big)
            new.append(big)
        return new
def top_k(lst, k):
    return sort_age(lst)[:k]
    pass

print(top_k([9, 8, 4, 5, 7, 2, 3, 1, 6], 5))