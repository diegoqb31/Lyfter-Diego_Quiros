from BinaryTree import BinaryTree
from Node import Node


def main():
    
    first_node = Node(1)
    second_node = Node(2)
    third_node = Node(6)
    fourth_node = Node(7)
    fifth_node = Node(5)
    my_binary_tree = BinaryTree()
    
    print(f"Insert de {first_node.data}")
    my_binary_tree.insert(first_node)
    my_binary_tree.print_structure()
    
    print(f"Insert de {second_node.data}")
    my_binary_tree.insert(second_node)
    my_binary_tree.print_structure()
    
    print(f"Insert de {third_node.data}")
    my_binary_tree.insert(third_node)
    my_binary_tree.print_structure()
    
    print(f"Insert de {fourth_node.data}")
    my_binary_tree.insert(fourth_node)
    my_binary_tree.print_structure()
    
    print(f"Insert de {fifth_node.data}")
    my_binary_tree.insert(fifth_node)
    my_binary_tree.print_structure()


main()