from Node import Node
from Linked_List import Linked_List

def kth_to_last(linked_list, k):
    #If k is non-positive, invalid k
    if k < 1:
        print("please insert a positive number")
        return
    
    curr = linked_list.head

    count = 0

    #count number of nodes
    while curr is not None:
        count += 1
        curr = curr.next

    #If less than k nodes, there is no kth last node
    if count < k:
        print("number too large")
        return None

    #reset curr
    curr = linked_list.head

    #iterate through until there are only k nodes left
    while count > k:
        curr = curr.next
        count -= 1
    
    #return the kth last node
    return curr.data

#This is O(N) time where N is the number of nodes
#First while loop goes through N nodes, so O(N)
#Second goes through at max N nodes, so also O(N)
#Thus total is O(N)

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

print(kth_to_last(link, 3))