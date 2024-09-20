#use circular linked list, make rotate method O(1) time with respect to length of the circular array, but O(N) time with respect to the num of indexes rotated
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Circular_Array:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head is None:
            self.head = node
            node.next = self.head #create circular linked list
        else:
            cur_node = self.head
            while cur_node.next is not self.head: #while next node isn't the head of the circle
                cur_node = cur_node.next #iterate

            cur_node.next = node #when at end of list, append the new node
            node.next = self.head #set the new node's next to the head to recreate the circle

    def rotate(self, num_indexes):
        if self.head is None: #if empty list, do nothing
            return
        elif self.head.next == self.head: #if only one element in list, do nothing
            return
        else:
            count = 0
            while count < num_indexes:
                self.head = self.head.next #keep iterating head num_indexes times (doesn't affect node connections, only affects "start" of the "circular array")
                count += 1
        
    def clear(self):
        self.head = None #deallocates all head node, which in turn deallocates all the following nodes

    def pop(self):
        if self.head is None: #if empty list, do nothing
            return
        
        cur_node = self.head
        prev_node = None
        #iterate through until cur_node is the last node in the circle
        while cur_node.next is not self.head:
            prev_node = cur_node
            cur_node = cur_node.next
        
        prev_node.next = self.head #skip over last node, which deallocates it

        return cur_node 


