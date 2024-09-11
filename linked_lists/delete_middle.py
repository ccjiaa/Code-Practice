from Node import Node
from Linked_List import Linked_List

def delete_middle(node):
   #if last node, then do nothing
   if node.next == None:
       return
  
   node.data = node.next.data #make this node a copy of the next node
   node.next = node.next.next #delete the next node by skipping over it

#This is O(1) time since we always do two units of constant work regardless of the size
# of the linked list the node is a part of

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

curr = link.head
while curr is not None:
    print(curr.data)
    curr = curr.next

delete_middle(c)
print('--------------------------------')

curr = link.head
while curr is not None:
    print(curr.data)
    curr = curr.next