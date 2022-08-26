def one_counter():
    temp = int(input('Type: '))
    x = one_counter()
    if temp[:1] == 1:
        return one_counter() + 1
    elif temp[:1] == 0:
        return 0
