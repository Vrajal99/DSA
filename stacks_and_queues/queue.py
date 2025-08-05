class Queue:
    def __init__(self):
        self.q=[]

    def enqueue(self,val):
        self.q.append(val)

    def dequeue(self):
        if not self.is_empty():
            return self.q.pop(0)
        return "Queue is Empty"
    
    def is_empty(self):
        return len(self.q)==0
    
    def peek(self):
        if not self.is_empty():
            return self.q[0]
        return "Queue is Empty"
    
    def display(self):
        print(f"Queue: {self.q}")

if __name__=="__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.display()
    print("Dequeued:", q.dequeue())
    print("Front Element:", q.peek())