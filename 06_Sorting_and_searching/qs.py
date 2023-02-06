from random import randint


def qs(lis):
    if len(lis) < 2:
        return lis

    mid = len(lis)//2
    elem = lis[mid]
    left = list(i for i in lis if i < elem)
    center = list(filter(lambda x: x == elem, lis))
    right = list(j for j in lis if j > elem)

    return qs(left) + center + qs(right)

if __name__ == '__main__':
    for i in range(10):
        lis = list(randint(0, 34) for i in range(10))
        print(lis)
        so = qs(lis)
        print('--->>', so)
        lis.sort()
        print('___<<', lis)