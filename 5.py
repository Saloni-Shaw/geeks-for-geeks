def rotate(arr):
  
    # store the last element in a variable
    lastElement = arr[-1]

    # assign every value by its predecessor
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]

    # first element will be assigned by last element
    arr[0] = lastElement

if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5]
  rotate(arr)
  for i in range(0, len(arr)):
    print(arr[i], end=' ')