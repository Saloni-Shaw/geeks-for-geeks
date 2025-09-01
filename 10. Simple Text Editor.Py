Q = int(input())
stack = ['']

for _ in range(Q):
    query = input().split()
    t = int(query[0])
    if t == 1:
        stack.append(stack[-1] + query[1])
    elif t == 2:
        k = int(query[1])
        stack.append(stack[-1][:-k])
    elif t == 3:
        k = int(query[1])
        print(stack[-1][k-1])
    else:
        stack.pop()
