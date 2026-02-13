from Node import Node

class Stack:
    top: Node

    def __init__(self):
        self.top = None


    def print_structure(self):
        current_node = self.top

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node


    def pop(self):
        if self.top is None:
            return None  
        
        removed = self.top
        self.top = self.top.next
        return removed
