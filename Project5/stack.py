class Stack:
    def __init__(self):
        self.lyst = []
        self.stacksize = 0
    
    def push(self, item):
        self.lyst.append(item)
        self.stacksize += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        self.stacksize -= 1
        return self.lyst.pop()
    
    def top(self):
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self.lyst[-1]
    
    def size(self):
        return self.stacksize
    
    def clear(self):
        self.stacksize = 0
        self.lyst = []

    def is_empty(self):
        return self.stacksize == 0