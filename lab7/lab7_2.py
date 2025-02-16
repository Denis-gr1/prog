def sum_nested_non_recursive(nested_list):
    total = 0
    stack = [nested_list] 

    while stack:
        current_list = stack.pop()
        for element in current_list:
            if isinstance(element, list):
                stack.append(element)
            else:
                total += element

    return total

result = sum_nested_non_recursive([1, [2, [3, 4, [5]]]])
print(result)