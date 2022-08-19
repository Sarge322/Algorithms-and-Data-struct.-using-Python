# Дано натуральное число n. Выведите все числа от 1 до n.

def sum_n(n):
    if n <= 0:
        return n
    else:
        return n + sum_n(n - 1)


if __name__ == '__main__':
    n = 10
    print(sum_n(n))
    print((1 + n) * n / 2)
    assert sum_n(n) == (1 + n) * n / 2, "Error!"
