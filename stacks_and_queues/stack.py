from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()

    def push(self,val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def isEmpty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

def reverse_string(s):
        
        stk=Stack()
        for chr in s:
            stk.push(chr)
        
        op=''
        while not stk.isEmpty():
            op+=stk.pop()
        return op

def is_balanced(s):
    brackets={'(':')','[':']','{':'}'}
    stk=Stack()

    for chr in s:
        if chr in brackets:
            stk.push(chr)
        if chr==')' or chr==']' or chr=='}':
            if stk.isEmpty():
                return False
            
            if chr !=brackets[stk.pop()]:
                return False
    return stk.size()==0


    pass

if __name__ =="__main__":
    stack=Stack()

    stack.push(20)
    stack.push(23)
    stack.push(22)
    stack.push(24)
    stack.push(201)

    print(stack.size())
    print(stack.isEmpty())
    print(stack.peek())

    s="We shall overcome."
    
    
    
    print(reverse_string(s))

    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))