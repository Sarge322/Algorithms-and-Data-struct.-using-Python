import timeit

popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
pz = popzero.timeit(number=1000)

x = list(range(2000000))
pd = popend.timeit(number=1000)

print("%15.5f, %15.5f" %(pz, pd))

print("pop(0), pop()")
for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pr = popzero.timeit(number=1000)
    print("%15.5f, %15.5f"%(pt, pr))