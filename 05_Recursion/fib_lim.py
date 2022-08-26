def fib(lim):
    res = [0, 1]
    i = 0
    j = 1
    while True:
        x = res[i] + res[j]

        if x < lim:
            res.append(x)
        else:
            return res
        i = i + 1
        j = j + 1


print(fib(999))


def fib_print(ind):
    fib1 = fib2 = 1

    print(fib1, fib2, end=' ')

    for i in range(ind):
        fib1, fib2 = fib2, fib2 + fib1
        print(fib2, end=' ')


if __name__ == '__main__':
    x = int(input('Type end ind of Fib row: '))
    fib_print(x)
