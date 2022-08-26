def rec_fib(num):
    if num in (1, 2):
        return 1
    i = rec_fib(num - 1)
    j = rec_fib(num - 2)
    return i + j


if __name__ == '__main__':
    x = int(input('Type: '))
    print(rec_fib(x))