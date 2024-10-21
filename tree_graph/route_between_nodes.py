from Graph import Graph
from Graph_Node import Graph_Node
from collections import deque

def route_between_nodes(node1, node2):
    #Create a deque for each of the nodes
    que1 = deque()
    que2 = deque()

    #Create a dict for each of the starting nodes to mark their visited nodes
    visited_1 = {}
    visited_2 = {}

    #Add each node to their respective dicts
    visited_1[node1] = 1
    visited_2[node2] = 1

    #Append each starting node to their queues for traversal
    que1.append(node1)
    que2.append(node2)

    #while the deque is not empty
    while que1 or que2: 
        #Initialize as None so that the following composite if statement is always valid 
        curr1 = None
        curr2 = None

        #If designated deque is not empty, pop and item from the front of said deque
        if que1:
            curr1 = que1.popleft()
        if que2:
            curr2 = que2.popleft()

        #If the current node is the opposite base node or has been visited on the path of the other base node (or vice-versa), return True
        if curr1 is node2 or curr2 is node1 or curr1 in visited_2 or curr2 in visited_1:
            return True
        else:
            #Else, place all child nodes of the current node in the deque and mark them as visited, then repeat the process
            if curr1 is not None:
                for adj_node in curr1.child_list:
                    if adj_node not in visited_1:
                        visited_1[adj_node] = 1
                        que1.append(adj_node)
            if curr2 is not None:
                for adj_node in curr2.child_list:
                    if adj_node not in visited_2:
                        visited_2[adj_node] = 1
                        que2.append(adj_node)

    #Fail-safe in case something wrong happens in the loop that prevented the nodes being detect in the opposite dict(s)
    if node1 in visited_2 or node2 in visited_1:
        return True
    
    #If not True then must be False
    return False


#As this is a bidirectional search, this is O(K^(d/2)) time, where k is the number of nodes in a single level and d is the depth

n1 = Graph_Node(1)
n2 = Graph_Node(2)
n3 = Graph_Node(3)
n4 = Graph_Node(4)

n1.append(n2)
n2.append(n3)

g = Graph([n1,n4])

print(route_between_nodes(n1, n3))
print(route_between_nodes(n1, n4))