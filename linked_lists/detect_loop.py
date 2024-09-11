from Node import Node
from Linked_List import Linked_List

#Important Assumption: The given linked_list is circular, otherwise this would be an infinite loop

def detect_loop(circle_list):
    curr = circle_list.head
    node_dict = {}

    while True:
        if curr not in node_dict:
            node_dict[curr] = curr
        else:
            return curr        #if the same node is passed over twice, it is the start of the loop
        curr = curr.next
    
    #if somehow the code glitches out of the loop, return None
    return None

#This is O(N) time, where N is the number of unique nodes
#This is because we pass through each unique node once before hitting a duplicate when we loop back
#Thus the time is actuall O(N + 1) which turns into O(N)
#Space complexity is also O(N) since we store O(N) unique nodes worth of data

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

link = Linked_List(a)
link.append(b)
link.append(c)
link.append(d)
link.append(e)
link.append(c)

print(detect_loop(link).data)