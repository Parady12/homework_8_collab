def reverse_ascending(numbers):
    sorted_result = sorted(numbers)
    reversed_result = reversed(sorted_result)
    return list(reversed_result)
print(reverse_ascending([1, 2, 3, 4, 5]))
print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]))
print(reverse_ascending([5, 4, 3, 2, 1]))
print(reverse_ascending([]))