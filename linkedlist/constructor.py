class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value=0):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def perpend(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        self.length+=1
    
    def pop(self):
        if self.length==0:
            return None
        sec_last=None
        start=self.head
        if self.length==1:
            self.head=None
            self.tail=self.head
            self.length-=1
            return start
        for i in range(self.length):
           if start.next.next==None:
               sec_last=start 
               break
           start=start.next
        ret_value=sec_last.next
        sec_last.next=None
        self.tail=sec_last
        self.length-=1
        return ret_value
    
    def insert(self,index,value):
        new_node=Node(value)
        if index>self.length or index<0:
            raise IndexError("index out of range")
        if index==0:
            self.perpend(value)
            return 
        elif index==self.length :
            self.append(value)
            return 
        elif index==1:
            new_node.next=self.head.next
            self.head.next=new_node
        else:
            start=self.head
            prev=None
            for i in range(index-1):
                prev=start
                start=start.next
            prev.next=new_node
            new_node.next=start
        self.length+=1

    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        if self.length==1:
            self.tail=None
        self.length-=1
        return temp
    
    def remove(self, index):
        if index>self.length-1 or index<0:
            raise IndexError("Index out of range")
        if index==0:
            return self.pop_first()
        if index==self.length-1:
           return  self.pop()
        prev_node=None
        temp_node=self.head
        for i in range(index):
            prev_node=temp_node
            temp_node=temp_node.next
        removed_node=prev_node.next
        prev_node.next=temp_node.next
        temp_node.next=None
        self.length-=1
        return removed_node

    def get(self,index):
        if index>self.length-1 or index<0:
            raise IndexError('Index out of range.')
        elif index==0:
            return self.head
        elif index==1:
            return self.head.next
        else:
            start=self.head
            for i in range(index):
                start=start.next
            return start
        
    def set(self,index,value):
        self.get(index).value=value
        return self.get(index)

    def reverse(self):
        if self.length==0:
            return 
        elif self.length==1:
            return
        else:
            temp=self.tail
            self.tail=self.head
            self.head=temp
            prev=None
            curr=self.tail
            next_=self.tail.next
            for i in range(self.length):
                curr.next=prev
                prev=curr
                curr=next_
                if i!=self.length-1:
                    next_=next_.next
    def find_middle_node(self):
        if self.length==1:
            return self.head
        elif self.length==0:
            return None
        slow_node=self.head
        fast_node=slow_node.next.next
        while fast_node:
            slow_node=slow_node.next
            fast_node=fast_node.next.next
        return slow_node
    def __str__(self):
        start=self.head
        if self.length==0:
            return "empty list :("
        for i in range(self.length):
            print(f"{start.value} -> ",end="")
            start=start.next
        print("none")
        return ""
    
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(2)
ll.append(1)