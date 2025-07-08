def remove_all_after(numbers, n):
    ...
    result = []
    for item in numbers: 
        result.append(item)
        if item == n:
            break
    return result

# print(remove_all_after([1, 2, 3, 4, 5], 3))
# print(remove_all_after([1, 1, 2, 2, 3, 3], 2))
# print(remove_all_after([], 3))
# print(remove_all_after([1, 2, 3], 8))