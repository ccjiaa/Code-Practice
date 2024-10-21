class Graph_Node:
    def __init__(self, data):
        self.data = data
        self.child_list = []
        self.parent = None

    def append(self, node):
        self.child_list.append(node)

    def print(self):
        return self.data