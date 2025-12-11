class Stack:
    def __init__(self):
        self.lyst = []
    
    def push(self, item):
        self.lyst.append(item)
    
    def pop(self):
        return self.lyst.pop()
    
    def top(self):
        return self.lyst[-1]
    
    def size(self):
        return len(self.lyst)
    
    def clear(self):
        self.lyst = []