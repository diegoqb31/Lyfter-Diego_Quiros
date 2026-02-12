class Node:
    data: str
    right: "Node"
    left: "Node"


    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None