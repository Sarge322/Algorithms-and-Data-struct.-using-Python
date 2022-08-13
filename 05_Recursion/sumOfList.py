def sum_of_list(ls):
    if len(ls) == 1:
        return ls

    middle = len(ls) // 2
    left = sum_of_list(ls[:middle])
    right = sum_of_list(ls[middle:])
    print(f'{left} <-----> {right}')

    j = left[0] if isinstance(left, list) else left
    x = right[0] if isinstance(right, list) else right
    print(x + j)

    return x + j


# sum_of_list([i for i in range(20)])

def calculate_sum_of_list_elements(values: list[int]) -> int:
    if len(values) == 1:
        return values[0]
    else:
        mid = len(values) // 2
        left = calculate_sum_of_list_elements(values[:mid])
        right = calculate_sum_of_list_elements(values[mid:])

    return left + right


calculate_sum_of_list_elements(([i for i in range(20)]))