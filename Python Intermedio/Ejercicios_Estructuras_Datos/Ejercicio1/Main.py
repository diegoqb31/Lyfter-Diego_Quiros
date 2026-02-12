from Stack import Stack
from Node import Node


def main():
    
    first_node = Node(41)
    second_node = Node(31)
    third_node = Node(31)
    fourth_node = Node(15)
    fifth_node = Node(9)
    my_stack = Stack()
    
    print(f"PUSH del nodo {first_node.data}")
    my_stack.push(first_node)
    my_stack.print_structure()
    
    print(f"PUSH del nodo {second_node.data}")
    my_stack.push(second_node)
    my_stack.print_structure()
    
    print(f"PUSH del nodo {third_node.data}")
    my_stack.push(third_node)
    my_stack.print_structure()
    
    print(f"PUSH del nodo {fourth_node.data}")
    my_stack.push(fourth_node)
    my_stack.print_structure()
    
    print(f"POP del nodo {fourth_node.data}")
    my_stack.pop()
    my_stack.print_structure()
    
    print(f"PUSH del nodo {fifth_node.data}")
    my_stack.push(fifth_node)
    my_stack.print_structure()


main()