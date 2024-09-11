#*****************************************************************************
    #This priority queue compares priorities and takes the larger value
    #Implements this queue using a linked list
#*****************************************************************************

#Class to create new node
#contains node data and node priority
class Node:
    def __init__(self, value, prio):
        self.value = value
        self.prio = prio
        self.next = None



#Implementation of priority_queue
class priority_queue:
    def __init__(self):
        self.queue_head = None

    #Method to check if priority_queue is empty
    #If yes, then return true
    #else, if not empty, return false
    def is_empty(self):
        if self.queue_head is None:
            return True
        return False
    

    #Method to push a new node into the queue according to prio
    def enqueue(self, value, prio):

        #create new node with parameters
        n = Node(value, prio)

        #if current queue is empty, set head to new node
        if self.is_empty():
            self.queue_head = Node
        else:

            #Check if new node is highest priority
            if self.queue_head.prio >= prio:

                #If so set old head as new node's next
                n.next = self.queue_head

                #Set head to the new node
                self.queue_head = n
            else:
                curr = self.queue_head
                prev = None
                while curr is not None:

                    #Check for when new node prio is greater than 
                    #prio of a node already in the queue
                    if curr.prio < prio:
                        break
                    prev = curr
                    curr = curr.next

                #insert the new node before the node whose prio is lower
                prev.next = n


    #Method to dequeue the node with the highest priority in the queue
    def dequeue(self):

        #Check for empty queue
        if self.is_empty():
            return
        else:

            #make a copy of the current head
            temp_head = self.queue_head

            #set current head's next value as the new head
            self.queue_head = self.queue_head.next

            return temp_head.value
    

    #Method to check the value of the node with the highest priority in the queue
    def peek(self):
        #Check for empty queue
        if self.is_empty():
            return
        else:
            return self.queue_head.value
    
