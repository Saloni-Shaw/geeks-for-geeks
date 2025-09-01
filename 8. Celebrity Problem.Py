def find_celebrity(M):
    n = len(M)
    candidate = 0
    for i in range(1, n):
        if M[candidate][i] == 1:
            candidate = i
    for i in range(n):
        if i != candidate and (M[candidate][i] == 1 or M[i][candidate] == 0):
            return -1
    return candidate

M = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]
print(find_celebrity(M))  
