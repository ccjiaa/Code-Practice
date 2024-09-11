from Node import Node
from Linked_List import Linked_List

def partition(linked_list, x):
    
    curr = linked_list.head
    prev = ""

    while curr is not None:
        if curr != linked_list.head:
            if curr.data < x:                        #if <, move to front (if >= , do nothing)
                prev.next = curr.next                #connect the new gap
                temp_head = linked_list.head         #temporarily store the head
                linked_list.head = curr              #set current node to be the head
                linked_list.head.next = temp_head    #set current node's next node to be the old head
                curr = prev                          #return curr to its previous traveled node
        prev = curr
        curr = curr.next                     #iterate
    
    return linked_list

#This is O(N) time as the while loop does consatnt work over N nodes

a = Node(9)
b = Node(3)
c = Node(2)
d = Node(5)
e = Node(1)

link = Linked_List(a)
link.append(b)
link.append(c)
link.append(d)
link.append(e)

curr = link.head

while curr is not None:
    print(curr.data)
    curr = curr.next

partition(link, 5)
print("-------------------------------------------------------")

curr = link.head

while curr is not None:
    print(curr.data)
    curr = curr.next