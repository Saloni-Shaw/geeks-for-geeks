def precedence(op):
    if op in '+-': return 1
    if op in '*/': return 2
    return 0

def infix_to_postfix(expr):
    stack = []
    output = ''
    for ch in expr:
        if ch.isalnum():
            output += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()  # remove '('
        else:
            while stack and precedence(stack[-1]) >= precedence(ch):
                output += stack.pop()
            stack.append(ch)
    while stack:
        output += stack.pop()
    return output

print(infix_to_postfix("a+b*(c-d)"))  
