from collections import deque
'''
binary search tree has left and right values
'''
class Node:
    def __init__(self,value):
        self.value=value
        self.left , self.right= None, None
    

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        prev = None
        curr = self.root
        while curr is not None:
            prev = curr
            if value < curr.value:  # Go left if value is smaller
                curr = curr.left
            else:  # Go right if value is greater or equal
                curr = curr.right

        if value < prev.value:
            prev.left = new_node
        else:
            prev.right = new_node

    def contains(self,value):
        curr=self.root
        while curr:
            if curr.value==value:
                return True
            if value>curr.value:
                curr=curr.right
            else :
                curr=curr.left
        return False
    
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

    


    


new_Tree=BinarySearchTree()
new_Tree.insert(3)
new_Tree.insert(2)
new_Tree.insert(4)
new_Tree.insert(8)
new_Tree.insert(6)
new_Tree.insert(3)
print(new_Tree.contains(69))
new_Tree.print_tree()