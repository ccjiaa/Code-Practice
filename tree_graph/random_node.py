import random
from collections import deque

class Random_Node_Binary_Tree:
    def __init__(self):
        self.root = None
        self.node_list = []
    
    
    #Method to get a random node from the tree
    def get_random_node(self):
        if len(self.node_list) < 1: #if no nodes yet
            return None
        
        random_idx = random.randrange(0, len(self.node_list)) #otherwise, pick a random index in the list

        return self.node_list[random_idx] #return the node at that random index


    #Method to insert a node into the tree
    def insert(self, new_node):
        # Create a deque for breadth-first-traversal
        q = deque()
        
        # Initially mark all the vertices as not visited
        # When we push a vertex into the q, we mark it as 
        # visited
        visited = {}

        # Mark the source node as visited and enqueue it
        visited[self.root] = True
        q.append(self.root)

        # Iterate over the queue
        while q:
            # Dequeue a vertex from queue
            curr = q.popleft()

            #If either the left child is empty of right child is empty, insert the new node
            if curr.left is None:
                curr.left = new_node
                return
            if curr.right is None:
                curr.right = new_node
                return
            
            #otherwise keep traversing by placing both child nodes in the queue
            visited[curr.left] = True
            q.append(curr.left)
            visited[curr.right] = True
            q.append(curr.right)

        self.node_list.append(new_node) #append the node to the node_list for random node

        return
    

    #Method to delete a node from the tree
    def delete(self, node):
        #find deepest node and replace the node to be deleted with that deepest node
        #then delete the last node from the tree
        #then find the node in node_list and delete it from the list
        #because both are O(N) time due to having to traverse all nodes in the worst case, the adding of node list does not increase the deletion time by a significant amount
        return


    #Method to check if a node is in the tree
    def find(self, node):
        if node in self.node_list:
            return True
        
        return False

