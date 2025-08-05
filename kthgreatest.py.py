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
    
def kth_greatest(input):
    nge=[-1]*len(input)
    st=Stack()

    for i in range(len(input)-1,-1,-1):
        while not st.isEmpty() and st.peek()<=input[i]:
            st.pop()
        if st.isEmpty():
            nge[i]=-1
        else:
            nge[i]=st.peek()
        
        st.push(input[i])
    return nge

def kth_greatest_2(input):
    n=len(input)
    nge=[-1]*n
    st=Stack()
    
    for i in range(2*n-1,-1,-1):
        while not st.isEmpty() and st.peek()<=input[i%n]:
            st.pop()
        if i<n:
            nge[i]= -1 if st.isEmpty() else st.peek()
        st.push(input[i%n])
    return nge

def nse(ip):
    n=len(ip)
    st=Stack()
    nse=[-1]*n

    for i in range(n):

        while not st.isEmpty() and st.peek()>ip[i]:
            st.pop()
        if st.isEmpty():
            nse[i]=-1
        else:
            nse[i]=st.peek()
        st.push(ip[i])
    return nse

if __name__=="__main__":

    arr=[4,12,5,3,1,2,5,3,1,2,4,6]

    print(kth_greatest(arr))

    arr=[2,10,12,1,11]

    print(kth_greatest_2(arr))

    arr=[4,5,2,10,8]

    print(nse(arr))