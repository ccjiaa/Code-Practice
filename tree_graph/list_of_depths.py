from Graph import Graph
from Graph_Node import Graph_Node
from collections import deque
from Node import Node
from Linked_List import Linked_List


def list_of_depths(root):
    que = deque()

    linked_list_list = []
    link_list_max_len = 1
    cur_link_list = None
    curr_node = None
    cur_len = 0

    que.append(root)

    while que:
        curr = que.popleft()
        curr_node = Node(curr.data)
        if cur_len == link_list_max_len:
            linked_list_list.append(cur_link_list)
            cur_len = 0
            link_list_max_len *= 2
            cur_link_list = Linked_List(curr_node)
        else:
            cur_link_list.append(curr_node)
        
        cur_len += 1

        for child in curr.child_list:
            que.append(child)