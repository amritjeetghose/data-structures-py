from collections import deque


class Stack:
    def __init__(self) -> None:
        self.container=deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)
    def __str__(self):
        return str(self.container)
    def reverse(self):
        return self.container.reverse()
s = Stack()
s.push(90)
print(s)
s.push(45)
s.push(60)
print(s)
s.pop()
print(s)
print(s.peek())
print(s.peek())
print(s.size())
s.reverse()
print(s)

