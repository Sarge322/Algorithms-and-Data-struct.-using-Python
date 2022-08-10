from random import randint
import os

def list_generator():
    letter_list = [chr(i) for i in range(97, 123)]
    letter_list.append(chr(32))
    result = []
    counter = 28
    while counter > 0:
        result.append(letter_list[randint(0, 26)])
        counter = counter - 1
    return result


def analyzer():
    target = "methinks it is like a weasel"
    try_counter = 0
    best_try_result = [''] * len(target)
    best_try_counter = 0
    while True:
        rand_result = list_generator()
        match_counter = 0
        if target == str(rand_result):
            print(f"Total match, {rand_result}")
            break
        for i in range(len(target)):
            if target[i] == rand_result[i]:
                best_try_result[i] = rand_result[i]
                break
        res = ''.join(x for x in best_try_result)

        print("Best result so far is: %s" % res)
        if res == target:
            break
        os.system('cls')
        try_counter = try_counter + 1


analyzer()
