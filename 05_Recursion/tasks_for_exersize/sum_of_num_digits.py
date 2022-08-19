# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется).


def sums(num):
    # breakpoint
    if num < 10:
        return num
    else:
        # last digit
        x = num % 10
        # next last digit
        y = sums((num - x) / 10)
        return x + y


print(sums(999))



