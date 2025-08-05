class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        node=Node(data, self.head)
        self.head=node
 
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data, None) 
        else:
            itr =self.head

            while itr.next:
                itr=itr.next
            itr.next=Node(data, None)
    
    def insert_values(self,data_list):
        self.head=None

        for data in data_list:
            self.insert_at_end(data)
    
    def print_list(self):
        if self.head is None:
            raise Exception("List is empty")
        
        itr = self.head
        ll_item=''

        while itr:
            ll_item+=str(itr.data)+'-->'
            itr=itr.next
        ll_item+='None'
        print(ll_item)
    
    def length_of_list(self):
        if self.head is None:
            return 0
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr=itr.next
        return count   

    def insert_at(self, idx,data):
        if idx<0 or idx>self.length_of_list():
            raise Exception('Invalid Index')
        
        if idx==0:
            self.insert_at_beginning(data)
            return
        
        count=0
        itr=self.head

        while itr:
            if count == idx-1:
                node=Node(data,itr.next)
                itr.next=node
                break 

            itr=itr.next
            count+=1
    
    def remove_at(self,idx):
        if idx<0 or idx>=self.length_of_list():
            raise Exception('Invalid Index')

        if idx==0:
            self.head=self.head.next
            return

        count=0
        itr=self.head

        while itr:
            if count==idx-1:
                itr.next=itr.next.next
                break

            count+=1
            itr=itr.next

    def insert_after_value(self, data_after,data_to_insert):
        if self.head is None:
            return
        
        itr =self.head

        while itr:
            if itr.data==data_after:
                node =Node(data_to_insert,itr.next)
                itr.next=node
                break
            
            itr =itr.next

    def remove_by_value(self,data):
        if self.head is None:
            print("List is Empty")
            return
        
        itr=self.head
        prev=None

        while itr:

            if itr.data==data: # check if the data is the first element itself, if yes, then shift the head to next element
                if itr==self.head:
                    self.head=itr.next
                else:
                    prev.next=itr.next
                return
            
            prev=itr
            itr=itr.next
        print('Value not found')

    def reverse(self):

        # use 3 ptr, and start by saving the value of curr.next in next, update curr.next link to prev, then prev = curr and curr=next(move to next)

        curr=self.head
        prev=None
        next=None

        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head= prev

    def exists(self,data):
        itr = self.head
        while itr:
            if itr.data==data:
                return True
            itr=itr.next
        return False
    
    def hasCycle(self):
        slow=self.head
        fast=self.head

        while fast and fast.next:
            slow = slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False


    def get_frequency_of(self,data):
        itr = self.head
        count=0

        while itr:
            if itr.data==data:
                count+=1
            itr=itr.next
        
        return count
  
    def middle_of_ll(self):
        slow,fast=self.head,self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow.data


if __name__ == '__main__':
    ll=LinkedList()

    ll.insert_at_end(24)
    ll.insert_at_end(42)
    ll.insert_at_end(24)
    ll.print_list()

    ll.insert_at_beginning(12)
    ll.insert_at_beginning(13)
    ll.insert_at_beginning(14)
    ll.print_list()

    print(ll.length_of_list())

    ll.insert_values(['alpha','beta','gamma','delta','phi','lambda'])
    ll.print_list()

    ll.insert_at(0,"ram")
    ll.insert_at(2,"fam")
    ll.print_list()

    ll.remove_at(2)
    ll.remove_at(0)
    ll.print_list()

    ll.insert_after_value('gamma','vrajal')
    ll.print_list()

    ll.remove_by_value('vrajal')
    ll.print_list()

    ll.remove_by_value('alpha') #first elememt
    ll.print_list()

    ll.remove_by_value('lambda') #last element
    ll.print_list()

    ll.remove_by_value('gjkfd')

    ll.reverse()
    ll.print_list()

    print("Exists or Search: ",ll.exists('phi'))

    ll = LinkedList()
    ll.insert_values([1, 2, 3, 4, 5,5,5,5,5])

    print(ll.get_frequency_of(6))    

    ll = LinkedList()
    ll.insert_values([1, 2, 3, 4,5, 6,7,8,9]) #odd elements

    print('Middle of LL for odd elements:',ll.middle_of_ll())

    ll.insert_values([1, 2, 3, 4]) #odd elements

    print('Middle of LL for even elements:',ll.middle_of_ll())


    # Manually creating a cycle: point the next of the last node to the second node
    head = ll.head
    second = head.next
    last = head
    while last.next:
        last = last.next
    last.next = second  # cycle here

    print("Has cycle:",ll.hasCycle())


    ll2 = LinkedList()
    ll2.insert_values([10, 20, 30, 40])
    print("Has cycle:", ll2.hasCycle())  # Should print False