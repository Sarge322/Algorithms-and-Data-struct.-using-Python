from random import randrange


def sort(ls):
    # iterate through list from second position (first count as sorted)
    for i in range(1, len(ls)):
        # take second element of list and his index
        current = ls[i]
        position = i
        # iterate through sorted part of list, trying to find greater val
        # and switch it and our current value
        count = 0
        while position > 0 and current < ls[position - 1]:
            ls[position] = ls[position - 1]
            position = position - 1
            count += 1
            print('c',count)
        ls[position] = current
        print('<------------>', i+1)

    return ls


if __name__ == '__main__':
    lst = [50, -18, 84, -15, 90, 26, 45, 41, 30, 96]
    print(lst)
    print(sort(lst))
