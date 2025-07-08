def replace_last(numbers):
    result = []
    if len(numbers) > 0:
        result.append(numbers[-1])
        numbers.remove(numbers[-1])
        for i in numbers:
            result.append(i)
    else:
        return numbers
    return result

print(replace_last([2, 3, 4, 1]))
print(replace_last([1, 2, 3, 4]))
print(replace_last([1]))
print(replace_last([]))
