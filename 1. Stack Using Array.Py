class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

s = Stack()
s.push(10)
s.push(20)
print(s.peek())  
print(s.pop())   
print(s.pop())   
print(s.pop())   
