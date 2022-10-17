from random import randrange


def shellSort(ls):
    # Start with a big gap, then reduce the gap
    size = len(ls)
    gap = size // 2
    switch = 0
    # Create gap for
    while gap > 0:

        for i in range(gap, size):
            temp = ls[i]
            j = i
            if j >= gap and ls[j - gap] > temp:
                print(ls[j - gap], j - gap, '-->', temp, j, 'sw: ', switch)
                switch += 1
                ls[j] = ls[j - gap]
                j -= gap

            # put temp (the original a[i]) in its correct location
            ls[j] = temp
        print('<------------------->')
        gap = gap // 2
    return ls


if __name__ == '__main__':
    lst = [51, 73, -19, -8, 97, 2, 59, 81, 38, -9, 52]
    print('Unsorted: ', lst)
    print('Sorted: ', shellSort(lst))
