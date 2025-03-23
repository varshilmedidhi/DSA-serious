"""
Heap is a  data struct which represents  some sort of hiarachy tree

where the Node's parent Nodes are greter and 
and children Nodes are lower the the current node

the height of the tree is log (n) ->  where n is the no.of nodes

in a heap we can have duplicates also which is not the same case in trees

heaps are not good for searching as they are not properley structured 

the only thing you use a heap for is to  keep track of the largest item at the top
and be able to quickly remove it.

and we will store it in a list and not in create  node class.

      lets say we have to represent a heap like this in a list then ... 

                      99
                   72    61
                  58 55 27 18    

    # there are two way to represent the heap in a list 
##### way one :-  (empty zero index)

    [ , 99 , 72 , 61 , 58 , 55 , 27 , 18]


------formula to find child of a parent node : -

    left_child = 2 * parent_index # to find the left child

    right_child = 2*parent_index+1 # to find the right child

-----formula to find parent of child node (remember that each parent has upto two children) :-  
    
    parent_index= left_child_index//2 or right_child_index//2

heap insert method  :- 

 -> lets say that we have a  heap like this and we want to insert a node of val 100 

                            99
                        72     61
                      58      

 ->  our first intuiton would be add 100 to the top of the heap but we are not gonna do that
-> instead we are going to add 100 to the next open space

                            99
                        72     61
                      58  100   

-> Now the tree looks complete and the we would move our hundred to the place it belongs to
-> Now compare 100 to it's parent(72) since 100 is greater that 72  we would swap them both
-> and we reapeat this process until 100 reaches it's  position.

                            99
                        100     61
                      58  72   

                           100
                        99     61
                      58  72   

-> we are going to do this process with a while loop until our value reaches the top of the list where we can't 
-> compare it any further , or else there if the parent node is greater than the current node 
-> these are the only two conditions which would cause our while loop to break. 

example 2 :-  insert 75 ?

                           100
                        99     61 \ ->  61< 75 so swap
                      58  72  75  /

                           100    \  -> 100 > 75 so stop
                        99     75 /
                      58  72  62 


--------- now lets look at the steps of adding 100 in a list form  -> 


[ , 99 , 72 , 61 , 58 ,   ,   ,   ]

step 1 :- adding 100 to the next empty space : -

 0  1    2    3    4     5   6   7    -> indexes for reference 

[ , 99 , 72 , 61 , 58 , 100 ,   ,   ]

step 2 : - find the parent node from the child node :- formula (parent_index= left_child_index//2 or right_child_index//2)

    index of 100 -> 5//2 -> 2 
    Number at index 2 -> 72
    is 72 > 100 or 72 < 100 ?
    ans : 72 < 100 so swap

 0  1    2    3    4     5   6   7   
[ , 99 , 100 , 61 , 58 , 72 ,   ,   ]

to the same until either on of the above conditions is met ... 

 0  1    2    3    4     5    6   7   
[ , 100 , 99  , 61 , 58 , 72 ,   ,   ] 

as 100 is at the top we stop. 

-------- now lets look at adding 75 to our list :- 

 0  1    2    3    4     5   6   7   
[ , 100 , 99 , 61 , 58 , 72 , 75  ,   ]

6//2 -> 3 (swap)

 0   1    2     3    4    5   6    7   
[ , 100 , 99 , 75 , 58 , 72 , 61  ,   ]

3//2 -> 1 (100>75) (no swap)(break)




###### way two : - (empty last  index)

 0    1    2    3    4     5   6   7  
[99 , 72 , 61 , 58 , 55 , 27 , 18,  ] -> len == 8

# finding the children 
left_child=2*parent_index+1
right_child=2*parent_index+2

# finding the parent

parent_index= (left_child-1)//2 or (right_child-1)//2



Big O of trees :- 

insert or remove only takes O(log n) as you are iterating throught the tree 
and making changes
"""

class MaxHeap:
    """
        we are representing our heap in way two (empty last index) way 
    """
    def __init__(self):
        self.heap=[]
    def _left_child(self,index):
        return 2 * index+1
    def _right_child(self,index):
        return 2*index+2
    def _parent(self,index):
        return (index-1)//2
    def _swap(self,index1,index2):
        self.heap[index1] , self.heap[index2] = self.heap[index2], self.heap[index1]
    def _sink_down(self,index):
        '''
        sinking down the top of the heap after removing the top and replacing the bottom
        '''
        max_index=index
        while True:
            left_index = self._left_child(index) 
            right_index = self._right_child(index)
            if (left_index<len(self.heap) and  # bound check if the tree is not complete 
                self.heap[left_index] > self.heap[max_index]):
                max_index=left_index # making max index left index if it is > curr index
            if (right_index<len(self.heap) and  # bound check if the tree is not complete 
                self.heap[right_index]>self.heap[max_index]):
                max_index=right_index  # making max index right index if it is > curr index
            if max_index!=index:
                self._swap(index,max_index) 
                index = max_index 
            else:
                return

    def insert(self,value):
        '''
         putting something at the bottom and bubbling it up to the top
        '''
        self.heap.append(value)
        curr=len(self.heap)-1
        while True:
            if curr == 0 or  self.heap[self._parent(curr)]>self.heap[curr]:
                break
            else:
                new_curr=self._parent(curr)
                self._swap(curr,self._parent(curr))
                curr=new_curr
    def remove(self):
        '''
        this method removes the top of the heap and rearranges the heap accrodingly
        '''
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        max_value = self.heap[0] # this is the max value at the top of the heap
        self.heap[0]=self.heap.pop() # take the last value in the heap and put it at the top
        self._sink_down(0) # sink down the top to it's appropriate position 
        return max_value

myHeap= MaxHeap()
myHeap.insert(95)
myHeap.insert(75)
myHeap.insert(80)
myHeap.insert(55)

print(myHeap.heap)

myHeap.insert(60)

print(myHeap.heap)

myHeap.insert(50)
myHeap.insert(65)

print(myHeap.heap)

myHeap.remove()

print(myHeap.heap)
