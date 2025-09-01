def min_reversals(expr):
    if len(expr) % 2 != 0:
        return -1
    stack = []
    for ch in expr:
        if ch == '{':
            stack.append(ch)
        else:
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(ch)
    red_len = len(stack)
    open_braces = 0
    while stack and stack[-1] == '{':
        stack.pop()
        open_braces += 1
    return (red_len // 2 + open_braces % 2)

print(min_reversals("}{{}}{{{"))  
