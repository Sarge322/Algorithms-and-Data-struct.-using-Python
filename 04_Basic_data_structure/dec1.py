def odd(ls1):
    res=[]
    for i in ls1:
        if i%2 == 0:
            res.append(i)
    return res

def decor_fifth(odd_func):
    def wrapper():
        res = odd_func()
        for i in res:
            if i%5!=0:
                res.pop[i]
        return res

    return wrapper()


odd = decor_fifth(odd([1,2,3,4,5]))