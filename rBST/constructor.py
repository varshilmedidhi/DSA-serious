class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
class rBST:
    def __init__(self):
        self.root=None
    def __r_contains(self,current_node,value):
        '''
        helper method for our r_contains button which would help users to determine if a 
        value is in the bst or not.
        '''
        if current_node==None: # the point where we reach the max depth of the tree and return false (base case)
            return False
        if value==current_node.value: # point where we find the value and return True another base case
            return True
        if value < current_node.value: # if the given value is less that the curr value
           return  self.__r_contains(current_node.left,value)   # search left
        else:  # if the given value is greater that the curr value
           return  self.__r_contains(current_node.right,value) # search right
    def r_contains(self,value): 
        '''
        this is the method which user calls and the we use self.__r_contains(self,current_node,value) -> helper method to determine if the node is in the tree
        '''
        return self.__r_contains(self.root,value)
    def __r_insert(self,curr_node,value):
        '''
        method - (1)- commented
        '''
        # if self.root==None: # if the tree is empty
        #     self.root=Node(value) # intialize the root with the given node value
        #     return 
        # if value>current_node.value: 
        #     if current_node.right:  # if value is greater than curr value and curr_node.right is present move to the right
        #         self.__r_insert(current_node.right,value)
        #     else:
        #         new_node=Node(value)
        #         current_node.right=new_node
        #         return
        # elif value<current_node.value:
        #     if current_node.left:
        #         self.__r_insert(current_node.left,value)
        #     else:
        #         new_node=Node(value)
        #         current_node.left=new_node
        #         return
        '''
        method 2 - uncommented (clever version)
        '''
        if curr_node==None: # the base case (this is where we know that we have to insert the given value)
           return Node(value) # create a new value and return it to the node
        if value > curr_node.value: # move right if the value is greater 
            curr_node.right = self.__r_insert(curr_node.right,value) # equating the pointer by calling the instance to the left
        elif value < curr_node.value: # move left if the value is smaller
            curr_node.left = self.__r_insert(curr_node.left,value) # equating the pointer by calling the instance to the right
        return curr_node # this would not be called until we have added the node succesfully and this always returns the root node.
    def r_insert(self,value):
       '''
       calling our helper funtion and equating the value it returns to the root (making the root point to the new binary tree.)
       '''
       self.root =  self.__r_insert(self.root,value)
    
    def min_value(self,current_node):
        '''
        determining the min value by going as left down the tree as possible.
        '''
        while current_node.left is not None: 
            current_node=current_node.left
        return current_node.value

    def __r_delete(self,current_node,value):
        '''
        helper method which would delete the given value if present.
        '''
        if current_node==None: # this would be the base case 
            return None
        if value>current_node.value: 
            current_node.right=self.__r_delete(current_node.right,value)
        elif current_node.value>value:
            current_node.left=self.__r_delete(current_node.left,value)
        else: # this is the node which we have to delete
            if current_node.left==None and current_node.right==None: # condition where we have reached the max depth and we don't have any other nodes 
                return None # this would make the value which is pointing to this be the 
            elif current_node.left==None:  #  if there is no left node then
                return current_node.right # return to  right as the top
            elif current_node.right==None: # else if there is no right node 
                return current_node.left # return the left as the top 
            else: # if there are two nodes present ? 
                sub_tree_min=self.min_value(current_node.right) # find the min value TO THE RIGHT using the min value helper method
                current_node.value=sub_tree_min #replace the currnet node value with the min value TO THE RIGHT
                current_node.right=self.__r_delete(current_node.right,sub_tree_min) # delete the min value 
        return current_node # return the newtree's root.
        
    def r_delete(self,value):
         self.__r_delete(self.root,value)    


    # you don't need to know this
    def print_tree(self):
        if not self.root:
            print("Empty tree")
            return
        def node_to_dict(node):
            if not node:
                return None
            
            result = {
                'value': node.value,
                'children': {}
            }
            
            if node.left:
                result['children']['left'] = node_to_dict(node.left)
            
            if node.right:
                result['children']['right'] = node_to_dict(node.right)
                
            return result
        
        tree_dict = node_to_dict(self.root)
        
        # Pretty print the dictionary
        def pretty_print_dict(d, indent=0):
            if d is None:
                return
                
            value_str = f"Node({d['value']})"
            indent_str = "  " * indent
            print(f"{indent_str}{value_str}: {{")
            
            if 'children' in d and d['children']:
                for direction, child in d['children'].items():
                    print(f"{indent_str}  '{direction}': ", end="")
                    if child:
                        print("")
                        pretty_print_dict(child, indent + 2)
                    else:
                        print("None,")
            
            print(f"{indent_str}}}")
        
        pretty_print_dict(tree_dict)


my_tree= rBST()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

'''
example 1 which checks if 21 is in the bst or not 
'''
print('bst contains 21: ')
print(my_tree.r_contains(21))



'''
example 2  which checks if 33 is in the bst or not 
'''

print('bst contains 33: ')
print(my_tree.r_contains(33))



print('min value :')
print(my_tree.min_value(my_tree.root.left))

print('min value to the right: ')
print(my_tree.min_value(my_tree.root.right))

# printing the tree. 
print('printing tree')
my_tree.print_tree()