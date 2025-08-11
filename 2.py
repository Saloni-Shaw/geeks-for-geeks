# Function to find largest element
def find_largest(arr):
    largest = arr[0]  # assume first element is largest
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Examples
print(find_largest([1, 8, 7, 56, 90]))  # Output: 90
print(find_largest([5, 5, 5, 5]))       # Output: 5
print(find_largest([10]))               # Output: 10
