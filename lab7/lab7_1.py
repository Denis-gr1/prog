def sum_nested_recursive(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):
            total += sum_nested_recursive(element)
        else:
            total += element
    return total


result = sum_nested_recursive([1, [2, [3, 4, [5]]]])
print(result)