from random import randrange


def merge_list(l_list, r_list):
    res = []
    i = j = 0

    while i < len(l_list) and j < len(r_list):
        if l_list[i] <= r_list[j]:
            res.append(l_list[i])
            i = i + 1
        else:
            res.append(r_list[j])
            j = j + 1
    res = res + l_list[i:] + r_list[j:]
    return res


def merge_sort(ls):
    if len(ls) == 1:
        return ls

    middle = len(ls) // 2

    left = merge_sort(ls[:middle])
    right = merge_sort(ls[middle:])

    return merge_list(left, right)


def sort_test():
    list1 = [randrange(-10, 10) for i in range(10)]
    res = merge_sort(list1)

    print(res)
    print(sorted(list1))
    assert res == sorted(list1), f"Error! res must be {sorted(list1)}"
    print('Well done!!!')


if __name__ == '__main__':
    sort_test()
