# Дано натуральное число N. Выведите все его цифры по одной,
# в обратном порядке, разделяя их пробелами или новыми строками.

# При решении этой задачи нельзя использовать строки, списки, массивы
# (ну и циклы, разумеется). Разрешена только рекурсия и целочисленная арифметика.

def reverse(num):
    ls = []
    if num < 10:
        ls.append(int(num))
        print(int(num)),
        return ls
    else:
        x = num % 10
        print(int(x.rstop)),
        ls.append(int(x))
        ls.extend(reverse((num - x) / 10))
        return ls


print(reverse(123))
