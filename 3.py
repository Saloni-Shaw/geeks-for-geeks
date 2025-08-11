def second_largest(arr):
    largest = second = -1  # assume -1 if not found
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num
    return second

# Examples
print(second_largest([12, 35, 1, 10, 34, 1]))  # Output: 34
print(second_largest([10, 5, 10]))             # Output: 5
print(second_largest([10, 10, 10]))            # Output: -1
