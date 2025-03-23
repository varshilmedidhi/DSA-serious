class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self,index):
        '''
        given a heap which is unorderd make it orderd min to max 
        '''
        # edge case 1 :  if one or both of the childs are not present
        # todo : have a min var which is currently set to index
        # todo : compare our value with the children node values and update the min var
        # todo : swap index , min and update index min
        # todo (edge case handel) : if left_child and right_child var should alway be less than the len of heap
        
        min_index=index
        while True:
            # calc left , right child of our curr index
            left_child=self._left_child(index)  
            right_child=self._right_child(index)
    
            # if value at min_index < any update min_index then child swap   
            if(left_child< len(self.heap) and self.heap[left_child]<self.heap[min_index]): 
                min_index=left_child
            if(right_child<len(self.heap) and self.heap[right_child]<self.heap[min_index]):
                min_index=right_child
            if min_index!=index:
                self._swap(index,min_index) # swapping index and min_index
                index=min_index # updating our index
            else:
                return

    def insert(self,value):
        '''
        adding the value at the end of the list and then shifting the value 
        accordingly to the pos where it belongs.
        '''
        # notes: 
        # [6,8,10,12 ,4]
        # todo : add to the end of the list
        # todo : compare it with its parent node
        # todo : if the node is bigger (swap)
        # todo : if the curr node is at the top of the heap or  if the value above is smaller than curr node (break)

        self.heap.append(value)
        curr=len(self.heap)-1
        while True:
            if curr==0 or self.heap[self._parent(curr)] < self.heap[curr]: # break if one of the condition is met
                break
            self._swap(curr,self._parent(curr)) # swaping values at curr index and self._parent(curr) index
            curr=self._parent(curr) # updating curr with our values new pos which is the parent pos
    def remove(self):
        '''
            should remove the top of the heap and add the last value of the heap to the top then sink down
            [2, 6, 4, 12, 8, 10]
            
        min- 10 -index
            6  4
           12   8
          
        '''
        # edge case 1: if list has 1 or 0 values 
        # todo: if length == 1 return that value and make the heap empty elif length==0 return None 
        if len(self.heap)==1:
            return self.heap.pop()
        if not self.heap:
            return None
        min_val=self.heap[0] # storing the min val
        self.heap[0]=self.heap.pop() # replacing the top with the last
        self._sink_down(0) # sinking it down
        return min_val # returning the min val
        
 