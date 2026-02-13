class Node:
    data: str
    next: "Node"
    previous: "Node"


    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous