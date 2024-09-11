from Node import Node
from Linked_List import Linked_List

def sum_lists_forwards(link_list_a, link_list_b):
    sum_a = 0
    sum_b = 0

    multiplier = 1

    curr_a = link_list_a.head

    #biggest digit in front, so multiply multiplier by 10 for each node
    #Use curr.next because head node's tens place multiplier is already accounted for
    while curr_a.next is not None:
        multiplier *= 10
        curr_a = curr_a.next

    curr_a = link_list_a.head #reset curr_a

    #multiply the node values by their power of 10
    while curr_a is not None:
        sum_a += curr_a.data * multiplier
        multiplier //= 10
        curr_a = curr_a.next

    multiplier = 1 #reset multiplier

    curr_b = link_list_b.head

    #biggest digit in front, so multiply multiplier by 10 for each node
    #Use curr.next because head node's tens place multiplier is already accounted for
    while curr_b.next is not None:
        multiplier *= 10
        curr_b = curr_b.next

    curr_b = link_list_b.head #reset curr_b

    while curr_b is not None:
        sum_b += curr_b.data * multiplier
        multiplier //= 10
        curr_b = curr_b.next

    total_sum = sum_a + sum_b

    #Find the last digit of the combined sum, place into new linked list
    total_sum_head = Node(total_sum%10)
    total_sum_list = Linked_List(total_sum_head)
    total_sum = total_sum//10

    while total_sum > 0:
        digit = total_sum%10      #find last digit
        n = Node(digit)

        temp_head = total_sum_list.head  #temporarily store current head
        total_sum_list.head = n          #add node as head
        n.next = temp_head               #attach the remainder of the original list

        total_sum = total_sum//10 #slice off last digit

    return total_sum_list

#This is O(a + b) time, since we need to iterate through both linked lists at least once to know their node values

a = Node(9)
b = Node(3)
c = Node(2)

d = Node(5)
e = Node(1)
f = Node(8)

link = Linked_List(a)
link.append(b)
link.append(c)

link_2 = Linked_List(d)
link_2.append(e)
link_2.append(f)

curr = link.head

while curr is not None:
    print(curr.data)
    curr = curr.next

print("-------")

curr = link_2.head

while curr is not None:
    print(curr.data)
    curr = curr.next

link_3 = sum_lists_forwards(link, link_2)

print("-------")

curr = link_3.head

while curr is not None:
    print(curr.data)
    curr = curr.next