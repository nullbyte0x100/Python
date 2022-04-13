class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def return_stack(self):
        return self.stack
    def top(self):
        return self.stack[len(self.stack)-1]
s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.return_stack())
s.pop()
print(s.return_stack())
print(s.top())
