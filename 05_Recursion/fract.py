def fractal(num):
    if num > 0:
        return fractal(num - 1) * num
    else:
        return 1


print(fractal(16))