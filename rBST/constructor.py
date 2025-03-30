class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
class rBST:
    def __init__(self):
        self.root=None
    def __r_contains(self,current_node,value):
        if current_node==None:
            return False
        if value==current_node.value:
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

print('bst contains 21: ')
print(my_tree.r_contains(5))

print('printing tree')
my_tree.print_tree()

