from Node import Node
from Linked_List import Linked_List

def remove_dupes(linked_list):
    #create a hashtable to hold unique values
    #create curr and prev to iterate through the linked list
    linked_list_dict = {}
    curr = linked_list.head
    prev = ""
    
    #iterate through entire linked list, if value in dict, remove
    while curr is not None:
        if curr.data in linked_list_dict:
            prev.next = curr.next                 #If in hashtable, prev stays in place (since curr is deleted)
        else:
            linked_list_dict[curr.data] = 1
            prev = curr                           #If not in hastable, travel as normal, prev = curr
        curr = curr.next                          #Iterate

    return linked_list


#This is O(N) time because we do constant work on N nodes

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('a')
e = Node('c')

link = Linked_List(a)
link.append(b)
link.append(c)
link.append(d)
link.append(e)

curr = link.head

while curr is not None:
    print(curr.data)
    curr = curr.next

remove_dupes(link)
print("--------------------------")

curr = link.head

while curr is not None:
    print(curr.data)
    curr = curr.next