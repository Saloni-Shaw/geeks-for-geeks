class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        if self.top is None:
            return None
        return self.top.val

    def is_empty(self):
        return self.top is None

s = Stack()
s.push(10)
s.push(20)
print(s.peek())  
print(s.pop())   
print(s.pop())   
print(s.pop())   
