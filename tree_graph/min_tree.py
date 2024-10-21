from Graph import Graph
from Graph_Node import Graph_Node
import copy

def min_tree(num_list):
    node = split(num_list, 0, len(num_list))
    tree = Graph([node])
    return tree


def split(num_list, start, end):
    # if len(num_list) == 2:
    #     new_node = Graph_Node(num_list[0])
    #     new_node2 = Graph_Node(num_list[1])
    #     new_node.append(new_node2)
    #     return new_node

    if len(num_list) < 2:
        return Graph_Node(num_list)
    
    mid = (start + end)//2
    curr = num_list[mid]
    curr_node = Graph_Node(curr)

    node1 = split(copy.deepcopy(num_list[start:(mid - 1)]), start, mid - 1)
    node2 = split(copy.deepcopy(num_list[(mid + 1):end]), mid + 1, end)
    curr_node.append(node1)
    curr_node.append(node2)

    return curr_node

li = [1, 2, 3, 4, 5, 6]

new_tree = min_tree(li)
print(new_tree.head_list[0].data)
lis = new_tree.head_list[0].child_list
print(lis[0].data, lis[1].data)
listy = lis[0].child_list
listo = lis[1].child_list
print(listy[0].data, listy[0].data, listo[0].data)

#What happened to 3 and 5??????
#pls just redo this