# Дано натуральное число N. Выведите слово YES, если число N
# является точной степенью двойки, или слово NO в противном случае.

def is_root(n):
    if n <= 2:
        if n == 2:
            return 'Yes'
        else:
            return 'No'
    else:
        return is_root(n / 2)


print(is_root(3))