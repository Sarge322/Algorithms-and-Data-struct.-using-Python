from random import randrange


def sel_sort(ls):
    ind = 0
    temp = ls[0]
    while True:
        size = len(ls) - 1
        for i in range(size - ind):
            if ls[i] > temp:
                temp = ls[i]
        ind = ind + 1
        temp2 = ls[size - ind]
        ls[size - ind] = temp
        temp = temp2
        if ind == size:
            return ls


if __name__ == '__main__':
    lis1 = [randrange(0, 11) for i in range(11)]
    print(lis1)
    print(sel_sort(lis1))
