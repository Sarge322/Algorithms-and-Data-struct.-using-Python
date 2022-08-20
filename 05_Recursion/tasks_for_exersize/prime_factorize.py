# Дано натуральное число n>1. Выведите все простые делители этого числа в порядке
# неубывания с учетом кратности. Алгоритм должен иметь сложность O(n√).
from random import randrange


def fact(num, f):
    ls = []
    if num / f == 1:
        ls.append(f)
        return ls
    elif num % f == 0:
        fact(num // f, f)
        ls.append(f)
        ls.extend(fact(num // f, f))
        return ls
    else:
        return fact(num, f + 1)


# num = f = int(input('Enter the number: '))

if __name__ == '__main__':
    for i in range(10):
        rand = randrange(333)
        res = fact(rand, 2)
        temp = 1
        for j in res:
            temp = temp * j
        assert rand == temp, f'Erron, {rand} != {temp}'
        print(res, " -> ", rand, "==", temp)
    print("Well done!!!")
