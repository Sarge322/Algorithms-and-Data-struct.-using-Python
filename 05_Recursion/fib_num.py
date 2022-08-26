def fib_val(ind):
    fib1 = fib2 = 1

    while ind > 0:
        fib1, fib2 = fib2, fib2 + fib1
        ind = ind - 1
    return fib2


if __name__ == '__main__':
    x = int(input('Type ind of Fib number -> '))-2
    print(fib_val(x))
