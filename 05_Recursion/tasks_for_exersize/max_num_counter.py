def maximum():
    temp = int(input('Type: '))
    if temp == 0:
        return 0, 0
    else:
        x = maximum()
        if x[0] < temp:
            return temp, 1
        elif x[0] == temp:
            return temp, x[1] + 1
        else:
            return x


if __name__ == '__main__':
    print(maximum())
