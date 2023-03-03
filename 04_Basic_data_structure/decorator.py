import time


def test_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('work time is: ', end - start)
        return res
    return wrapper

@test_time
def some_func(a, b):
    while a != b:
       if a > b:
            a = a-b
       else:
           b = b - a
    return a
@test_time
def fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

# some_func=test_time(some_func)
# fast_nod=test_time(fast_nod)
res1 = fast_nod(2, 1000000)
res = some_func(2, 1000000)
print(res)
print(res1)