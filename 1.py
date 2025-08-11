# Function to insert at the end
def insert_at_end(arr, val):
    arr.append(val)  # append adds element at the end
    return arr

# Example usage
arr1 = [1, 2, 3, 4, 5]
val1 = 90
print(insert_at_end(arr1, val1))  # Output: [1, 2, 3, 4, 5, 90]

arr2 = [1, 2, 3]
val2 = 50
print(insert_at_end(arr2, val2))  # Output: [1, 2, 3, 50]
