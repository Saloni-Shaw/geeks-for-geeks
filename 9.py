def countFreq(arr):
    n = len(arr)
    
    # Mark all array elements as not visited
    visited = [False] * n
    ans = []
    for i in range(n):
        
        # Skip this element if already processed
        if visited[i]:
            continue
        
        # store the frequency
        count = 1
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1
        ans.append([arr[i], count])
    return ans

if __name__ == '__main__':
    arr = [10, 20, 10, 5, 20]
    ans = countFreq(arr)
    ans.sort(key=lambda x: x[0])
    for x in ans:
        print(x[0], x[1])