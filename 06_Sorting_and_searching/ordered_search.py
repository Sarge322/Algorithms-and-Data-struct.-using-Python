def ord_search(ls, item):
    ind = 0
    while True:
        if ind < len(ls):
            if ls[ind] < item:
                ind = ind + 1
            elif ls[ind] > item or (ind == len(ls) - 1 and ls[ind] != item):
                return False
            else:
                return True
        else:
            return False



def ord_search_test():
    ls = [i for i in range(11)]
    res = ord_search(ls, 3)
    assert res == True, f"Failure, {res} != 3"
    res = ord_search(ls, 10)
    assert res == True, f"Failure, {res} != False"
    res = ord_search(ls, 2)
    assert res == True, f"Failure, {res} != 2"
    print("Well done!!")


if __name__ == '__main__':
    ord_search_test()
