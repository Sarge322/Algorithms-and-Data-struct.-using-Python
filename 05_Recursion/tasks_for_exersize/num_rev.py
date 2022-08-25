def num_reverse(num, rev_num):
    temp = rev_num*10 + num%10
    if num > 10:
        temp = num_reverse(num//10, temp)
    return temp


if __name__ == '__main__':
    print(num_reverse(123456, 0))