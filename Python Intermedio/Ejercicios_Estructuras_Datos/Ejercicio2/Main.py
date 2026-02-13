from Double_Ended_Queue import Double_Ended_Queue
from Node import Node


def main():
    
    first_node = Node(41)
    second_node = Node(31)
    third_node = Node(31)
    fourth_node = Node(15)
    fifth_node = Node(9)
    my_double_ended_queue = Double_Ended_Queue()
    
    print(f"PUSH_RIGT del nodo {first_node.data}")
    my_double_ended_queue.push_right(first_node)
    my_double_ended_queue.print_structure_left_to_right()
    
    print(f"PUSH_RIGT del nodo {second_node.data}")
    my_double_ended_queue.push_right(second_node)
    my_double_ended_queue.print_structure_left_to_right()
    
    print(f"PUSH_RIGT del nodo {third_node.data}")
    my_double_ended_queue.push_right(third_node)
    my_double_ended_queue.print_structure_left_to_right()
    
    print(f"PUSH_LEFT del nodo {fourth_node.data}")
    my_double_ended_queue.push_left(fourth_node)
    my_double_ended_queue.print_structure_left_to_right()
    
    print(f"POP_RIGHT del nodo {fourth_node.data}")
    my_double_ended_queue.pop_right()
    my_double_ended_queue.print_structure_left_to_right()
    
    print(f"PUSH_LEFT del nodo {fifth_node.data}")
    my_double_ended_queue.push_left(fifth_node)
    my_double_ended_queue.print_structure_left_to_right()
    
    print(f"POP_LEFT del nodo {first_node.data}")
    my_double_ended_queue.pop_left()
    my_double_ended_queue.print_structure_left_to_right()


main()