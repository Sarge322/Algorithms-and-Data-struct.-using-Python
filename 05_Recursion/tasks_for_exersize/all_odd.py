# Дана последовательность натуральных чисел (одно число в строке), завершающаяся числом 0. Выведите все нечетные числа
# из этой последовательности, сохраняя их порядок.

# В этой задаче нельзя использовать глобальные переменные и передавать какие-либо параметры в рекурсивную функцию.
# Функция получает данные, считывая их с клавиатуры. Функция не возвращает значение, а сразу же выводит
# результат на экран. Основная программа должна состоять только из вызова этой функции.


def odd(ls1):
    if ls1 == []:
        return
    elif ls1[0] % 2 != 0:
        print(ls1[0], end=' ')
        odd(ls1[1:])
    else:
        odd(ls1[1:])


if __name__ == '__main__':
    x = input("Enter numbers sequence: ")
    ls = []
    try:
        for i in range(len(x)):
            ls.append(int(x[i]))
    except:
        print('Error! Type numbers only!')
    print(ls)
    odd(ls)