from Node import Node
from Linked_List import Linked_List

def sum_lists_backwards(link_list_a, link_list_b):
   multiplier = 1
   sum_a = 0
   sum_b = 0

   #Find the sum that linked list a represents
   curr_a = link_list_a.head
   while curr_a is not None:
       sum_a += curr_a.data * multiplier
       multiplier *= 10                    #Multiplier increases by x10 for each tens place
       curr_a = curr_a.next

   multiplier = 1 #reset multiplier

   #Find the sum that linked list b represents
   curr_b = link_list_b.head
   while curr_b is not None:
       sum_b += curr_b.data * multiplier
       multiplier *= 10                     #Multiplier increases by x10 for each tens place
       curr_b = curr_b.next

   total_sum = sum_a + sum_b                #Find combined sum

    #Find the last digit of the combined sum, place into new linked list
   total_sum_head = Node(total_sum%10)
   total_sum_list = Linked_List(total_sum_head)
   total_sum = total_sum//10

   curr_tot = total_sum_list.head
   while total_sum > 0:
       digit = total_sum%10      #find last digit
       n = Node(digit)

       curr_tot.next = n             #add node
       curr_tot = n                  #travel to node

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

link_3 = sum_lists_backwards(link, link_2)

print("-------")

curr = link_3.head

while curr is not None:
    print(curr.data)
    curr = curr.next