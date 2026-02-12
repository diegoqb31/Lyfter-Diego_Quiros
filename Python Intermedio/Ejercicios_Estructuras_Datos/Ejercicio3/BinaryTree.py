from Node import Node

class BinaryTree:
    
    def __init__(self):
        self.root = None

    def insert(self, new_node : Node):
        
        current_node = self.root
        if current_node:
            
            while current_node:
          
                if new_node.data < current_node.data:
                    
                    if current_node.left == None :
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                        
                else:
                    
                    if current_node.right == None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right
        else:
            
            self.root = new_node
    
    
    def print_structure(self):
        self.print_structure_recursive(self.root)
    
    
    def print_structure_recursive(self, current_node):
        if current_node is not None:
            self.print_structure_recursive(current_node.left)
            print(current_node.data)
            self.print_structure_recursive(current_node.right)