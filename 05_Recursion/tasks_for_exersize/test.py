def tes():
    l = int('1234551151')
    x = l % 10
    j = l % 100
    return x, (j - x) // 10


print(tes())
