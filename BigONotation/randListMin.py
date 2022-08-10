import random

rand_list = list(random.sample(range(100), 100))


def min_x(x):
    rand_list.sort()
    return rand_list[x]


print(min_x(5))
