# Дана последовательность натуральных чисел (одно число в строке), завершающаяся числом 0. Определите значение второго
# по величине элемента в этой последовательности, то есть элемента, который будет наибольшим, если из
# последовательности удалить наибольший элемент.
# В этой задаче нельзя использовать глобальные переменные. Функция получает данные, считывая их с клавиатуры,
# а не получая их в виде параметра. В программе на языке Python функция возвращает результат в виде кортежа из
# нескольких чисел и функция вообще не получает никаких параметров. В программе на языке C++ результат записывается
# в переменные, которые передаются в функцию по ссылке. Других параметров, кроме как используемых для возврата значения,
# функция не получает.
# Гарантируется, что последовательность содержит хотя бы два числа (кроме нуля).


def second_max():
    temp = int(input("Type num (0 -> execute): "))
    if temp == 0:
        return [0, 0]
    else:
        res = second_max()
        if res[0] < temp:
            res[1] = res[0]
            res[0] = temp
        elif res[0] > temp > res[1]:
            res[1] = temp
        return res


if __name__ == '__main__':
    print(second_max()[1])