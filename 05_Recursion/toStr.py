def toStr(n, base):
    convertString = "0123456789ABCDF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]


print(toStr(10, 2))

def rec(num1, num2):
    if num1 > num2:
        pass