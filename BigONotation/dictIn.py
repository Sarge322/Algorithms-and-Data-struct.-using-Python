import timeit
import random

for i in range(20, 70, 40):
    t = timeit.Timer("random.randrange(%d) in x" % (i * 10),
                     "from __main__ import random, x")
    ind = timeit.Timer("x[random.randrange(%d)]" % i,
                       "from __main__ import random, x")
    get_dict = timeit.Timer("x.get(random.randrange(%d))" % i,
                            "from __main__ import random, x")
    change_dict = timeit.Timer("x[(random.randrange(%d))] = %i" % (i, i),
                               "from __main__ import random, x")
    del_time = timeit.Timer("del x[random.randrange(%d)]" % i,
                            "from __main__ import random, x")

    x = list(range(i))
    # lst_time = t.timeit(number=1000)
    # ind_search = ind.timeit(number=10000)
    del_list = del_time.timeit(number=100)

    x = {j: i for j in range(i)}
    # d_time = t.timeit(number=1000)
    # g_dict = get_dict.timeit(number=1000)
    # c_dict = change_dict.timeit(number=1000)
    # del_dict = del_time.timeit(number=5)
    # print("%d, %10.3f, %10.5f, %10.8f" % (i, lst_time, ind_search, d_time))
    print("%d, %10.5f" % (i, del_dict))
