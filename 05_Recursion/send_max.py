def second_top():
    temp = int(input("Type: "))
    if temp == 0:
        return 0, 0
    else:
        res = second_top()
        if temp > res[0]:
            return temp, res[0]
        elif res[0] > temp > res[1]:
            return res[0], temp
        else:
            return res


if __name__ == '__main__':
    print(second_top()[1])