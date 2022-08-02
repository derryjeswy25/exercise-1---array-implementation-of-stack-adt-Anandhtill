import os

class Stack:
    def __init__(self, size):
        self.item = []
        self.size = size
        

    def is_empty(self):
        # Write code here
        if len(self.item)==0 :
            return True

    def is_full(self):
        # Write code here
        if len(self.item)==self.size :
            return True

    def push(self, data):
        if not self.is_full():
            self.item.append(data)

    def pop(self):
        if not self.is_empty():
            self.item.pop()

    def status(self):
        if not self.is_empty():
            for i in self.item:
                print(i)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
