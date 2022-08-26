from random import randint


def o_search(ls1, item):
    # return None if there is no item in the list in the end of the list
    if len(ls1) == 1 and ls1[0] != item:
        return
    # if 2 or more nums in list we compare them with middle element in list to know direction
    if len(ls1) >= 2:
        j = len(ls1) // 2
        # fount item in list and return it
        if ls1[j] == item:
            return item
        elif ls1[j] > item:
            return o_search(ls1[:j], item)
        elif ls1[j] < item:
            return o_search(ls1[j:], item)
    else:
        return ls1[0]


def o_search_test():
    for i in range(10):
        x = randint(0, 10)
        ls = [i for i in range(11)]
        res = o_search(ls, 13)
        assert res is None, f'Error, {res} != None'
        res = o_search(ls, x)
        assert res == x, f'Error, {res} != {x}'
        res = o_search(ls, x)
        assert res == x, f'Error, {res} != {x}'

        print('Test is good!')


if __name__ == '__main__':
    o_search_test()
