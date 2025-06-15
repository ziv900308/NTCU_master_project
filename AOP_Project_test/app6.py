# def error_function():
#     ahsdkjfh
#     adsfjojinJKNijk

#     asndfljknsadlkf
#     sajfnaklsjn
#     lasdnfkljasdnlfi
#     al;sdjnfmolasdng;KeyboardInterruptaldsfjngkjadsf

# print("This is app6.py")
# error_function()


def logAround(func):

    def wrapper(*args, **kwargs):
        # print('This is AroundBefore...')
        # print('This is AroundAfter...')
        
        # print(args, kwargs)
        print("This is logAround...")
        for i in range(len(args[1])):
            if args[0] <= args[1][i]:
                return i
            else:
                pass
        return len(args[1])
    return wrapper

# @logAround
# def error_function(e, lst):
#     ahsdkjfh
#     adsfjojinJKNijk
#     asndfljknsadlkf
#     sajfnaklsjn
#     lasdnfkljasdnlfi
#     al
#     sdjnfmolasdng
#     KeyboardInterruptaldsfjngkjadsf

# print('This is app6.py')
# print(error_function())



@logAround
def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i ]:
            return i
        
    return len(seq)

print(search(42, (-5, 1, 3, 5, 7, 10)))