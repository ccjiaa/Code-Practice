class Graph:
    def __init__(self, head_list):
        self.head_list = head_list

    def append(self, node):
        self.head_list.append(node)