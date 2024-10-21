class Binary_Tree_Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def append_left(self, node):
        self.left = node

    def append_right(self, node):
        self.right = node