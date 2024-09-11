from Node import Node
from Linked_List import Linked_List

def is_palindrome(linked_list):
    cur = linked_list.head

    node_stack = [] #declare stack

    #put every node in the stack
    while cur is not None:
        node_stack.append(cur.data) 
        cur = cur.next
    
    cur = linked_list.head #reset cur to head

    while cur is not None:
        top = node_stack.pop() #take the last appended value
        if cur.data != top:         #if not equal, not a palindrome
            return False
        
        cur = cur.next         #iterate

    return True

#This is O(N) time, since both while loops do at most N units of constant work, where N = # of nodes
#This is also O(N) space complexity since we make a stack containing all N nodes

a = Node('a')
b = Node('b')
c = Node('c')
b2 = Node('b')
a2 = Node('a')

x = Node('x')
y = Node('y')
z = Node('z')

link = Linked_List(a)
link.append(b)
link.append(c)
link.append(b2)
link.append(a2)

link_2 = Linked_List(x)
link_2.append(y)
link_2.append(z)

print(is_palindrome(link))
print(is_palindrome(link_2))