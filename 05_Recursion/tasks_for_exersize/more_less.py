# Даны два целых числа A и В (каждое в отдельной строке). Выведите все числа от A до B включительно, в порядке
# возрастания, если A < B, или в порядке убывания в противном случае.

def more_less(a, b):
    print(a)
    if a == b:
        return a
    else:
        return more_less(a + 1, b) if a < b else more_less(a - 1, b)


more_less(6, 3)
print()
more_less(2, 7)
