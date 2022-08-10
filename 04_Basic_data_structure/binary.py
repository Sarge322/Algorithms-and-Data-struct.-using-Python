from stack import Stack


def binary(number, div):
    digits = "0123456789ABCDEF"
    s = Stack()
    while number > 0:
        s.push(number % div)
        number = int(number / div)
    out = ''
    while not s.isEmpty():
        out = out + digits[s.pop()]
    return out


print(binary(256 , 16))
print(binary(17 , 2))
print(binary(45 , 2))
print(binary(96 , 2))
