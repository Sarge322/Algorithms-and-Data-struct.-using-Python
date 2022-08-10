mynum = [0, 0, 1]


def smp(numb):
    min1 = numb[0]
    min2 = numb[1]

    for i in numb[2:]:
        if min1 > i:
            if min1 < min2:
                min2 = min1
            min1 = i
        if min2 > i > min1:
            min2 = i

    return min1 if min1 > min2 else min2

print(smp(mynum))