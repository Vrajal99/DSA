class Stack():
    def __init__(self):
        self.stack=[]
    
    def push(self, val):
        self.stack.append(val)
        print(f"pushed {val}")
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "stack is empty"
    
    def display(self):
        print("stack", self.stack)

    def is_empty(self):
        return len(self.stack)==0

if __name__=="__main__":
    s=Stack()

    s.push(3)
    s.push(2)
    s.push(1)
    s.push(22)

    print(s.peek())

    s.display()

    s.pop()
    s.display()