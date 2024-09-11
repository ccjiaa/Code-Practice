from Node import Node
from Linked_List import Linked_List

def is_intersect(link_list_a, link_list_b):
    curr_a = link_list_a.head
    curr_b = link_list_b.head

    len_a = 0
    len_b = 0

    #find list length and last node
    while curr_a is not None:
        len_a += 1
        tail_a = curr_a
        curr_a = curr_a.next


    #find list length and last node
    while curr_b is not None:
        len_b += 1
        tail_b = curr_b
        curr_b = curr_b.next

    if tail_a != tail_b:
        return None             #last nodes different, no intersection
    
    diff_counter = 0
    longer_list = link_list_a         #initial value is arbitrarily chosen as list a
    shorter_list = link_list_a        #initial value is arbitrarily chosen as list a

    #find difference in number of nodes between the two lists
    #identify the longer list and shorter list
    if len_a == len_b:
        diff_counter = 0
    elif len_a > len_b:
        diff_counter = len_a - len_b
        longer_list = link_list_a
        shorter_list = link_list_b
    else:
        diff_counter = len_b - len_a
        longer_list = link_list_b
        shorter_list = link_list_a

    curr_long = longer_list.head
    curr_short = shorter_list.head

    #iterate through the difference in number of nodes to have the same number of remaining nodes
    while diff_counter > 0:
        curr_long = curr_long.next
        diff_counter -= 1

    #number of nodes after the intersection is the same, ignoring the extra nodes at the beginning of
    # the longer list ensures both lists will hit the intersection node at the same time
    while curr_long != curr_short:

        curr_long = curr_long.next
        curr_short = curr_short.next

    #both curr_short and curr_long are the same, arbitrarily choose to return curr_long
    return curr_long

#This is O(a + b) time, wher a and b are the lengths of the two lists respectively
#First two while loops are O(a) and O(b) respectively, since we iterate through each node. Adds up to O(a + b)
#If statements are O(1), absorbed
#Third while loop will always be shorter than either fo the first two loops, absorbed
#Last while loop is again shorter than the longer list, absorbed
#Thus total is O(a + b) time
#This is also O(1) space complexity

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
one = Node('1')
two = Node('2')
three = Node('3')
four = Node('4')

link = Linked_List(a)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

link_2 = Linked_List(one)
one.next = two
two.next = three
three.next = four
four.next = d
d.next = e
e.next = f

print(is_intersect(link, link_2).data)

#Earlier attempt (no hints). O(a + b) time complexity, O(a + b) space complexity:
#-----------------------------------------------------------------------------------------------------------------
# def is_intersect(link_list_a, link_list_b):
#     node_a_stack = []
#     node_b_stack = []

#     curr_a = link_list_a.head
#     curr_b = link_list_b.head

#     #put all nodes into a stack
#     while curr_a is not None:
#         node_a_stack.append(curr_a)
#         curr_a = curr_a.next

#     #put all nodes into a stack
#     while curr_b is not None:
#         node_b_stack.append(curr_b)
#         curr_b = curr_b.next

#     #if intersection exists, all the nodes after intersection will be same in both lists
#     #node after first node pair with different values is the intersecting node
#     while len(node_a_stack) > 0 and len(node_b_stack) > 0:
#         intersect = removed_a
#         removed_a = node_a_stack.pop()
#         removed_b = node_b_stack.pop()

#         if removed_a != removed_b:
#             return intersect
    
#     #if traveled through entire while loop, means all values are the same, the head is the intersect
#     return link_list_a.head
#------------------------------------------------------------------------------------------------------------------