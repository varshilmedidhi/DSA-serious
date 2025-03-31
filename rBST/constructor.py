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
        if current_node==None: # the point where we reach the max depth of the tree and return false
            return False
        if value==current_node.value: # point where we find the value and return True
            return True
        if value < current_node.value:
           return  self.__r_contains(current_node.left,value)
        else:
           return  self.__r_contains(current_node.right,value)
    def r_contains(self,value):
        return self.__r_contains(self.root,value)
    def __r_insert(self,current_node,value):
        if self.root==None:
            self.root=Node(value)
            return
        if value>current_node.value:
            if current_node.right:
                self.__r_insert(current_node.right,value)
            else:
                new_node=Node(value)
                current_node.right=new_node
                return
        elif value<current_node.value:
            if current_node.left:
                self.__r_insert(current_node.left,value)
            else:
                new_node=Node(value)
                current_node.left=new_node
                return
    def r_insert(self,value):
        self.__r_insert(self.root,value)
    
    def min_value(self,current_node):
        '''
        determining the min value 
        '''
        while current_node.left is not None:
            current_node=current_node.left
        return current_node.value

    def __r_delete(self,current_node,value):
        if current_node==None:
            return None
        if value>current_node.value:
            current_node.right=self.__r_delete(current_node.right,value)
        elif current_node.value>value:
            current_node.left=self.__r_delete(current_node.left,value)
        else:
            if current_node.left==None and current_node.right==None:
                return None
            elif current_node.left==None:
                current_node=current_node.right
            elif current_node.right==None:
                current_node=current_node.left
            else:
                sub_tree_min=self.min_value(current_node.right)
                current_node.value=sub_tree_min
                current_node.right=self.__r_delete(current_node.right,sub_tree_min)
        return current_node
        
    def r_delete(self,value):
        return self.__r_delete(self.root,value)    

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