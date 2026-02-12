from Node import Node

class Double_Ended_Queue:
    Head: Node
    Tail: Node
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def init_push(self, new_node):
        if self.head == None and self.tail == None:
            self.head, self.tail = new_node, new_node
            return True
        return False
    
    
    def push_left(self, new_node):
        if not self.init_push(new_node):
            new_node.next = self.tail
            self.tail.previous = new_node
            self.tail = new_node
    
    
    def push_right(self, new_node):
        if not self.init_push(new_node):
            new_node.previous = self.head
            self.head.next = new_node
            self.head = new_node
    
    
    def print_structure_left_to_right(self):
        current_node = self.tail
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
            
    
    def print_structure_right_to_left(self):
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.previous
    
    
    def pop_right(self):
        if self.head is None:
            return None

        removed = self.head

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.previous
            self.head.next = None

        return removed



    def pop_left(self):
        if self.tail is None:
            return None

        removed = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.next
            self.tail.previous = None

        return removed
