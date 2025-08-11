def move_zeros(arr):
    pos = 0  # index for placing non-zero elements
    
    # Move non-zero elements forward
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    
    # Fill remaining positions with 0
    while pos < len(arr):
        arr[pos] = 0
        pos += 1
    
    return arr

# Examples
print(move_zeros([1, 2, 0, 4, 3, 0, 5, 0]))  # [1, 2, 4, 3, 5, 0, 0, 0]
print(move_zeros([10, 20, 30]))              # [10, 20, 30]
print(move_zeros([0, 0]))                    # [0, 0]
