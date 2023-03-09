def odd(ls1):
    res=[]
    for i in ls1:
        if i%2 == 0:
            res.append(i)
    return res

def decor_every_third(odd_func):
    def wrapper(*args):
        odd()

