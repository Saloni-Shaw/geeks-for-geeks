def stock_span(prices):
    stack = []
    result = []
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] <= price:
            stack.pop()
        if not stack:
            result.append(i + 1)
        else:
            result.append(i - stack[-1])
        stack.append(i)
    return result

print(stock_span([100, 80, 60, 70, 60, 75, 85]))  
