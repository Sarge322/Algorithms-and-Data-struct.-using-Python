from random import randint


def search(ls, item):
    for i in ls:
        if i == item:
            return True


if __name__ == '__main__':
    ls1 = [i for i in range(10)]
    for i in range(20):
        print(search(ls1, randint(0, 20)))
