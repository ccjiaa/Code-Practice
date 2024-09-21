class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def __init__(self, node):
        self.head = node

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            cur = self.head:
            while cur.next is not None:
                cur = cur.next
            
            cur.next = node

    def delete(self, node):
        cur = self.head
        prev = None

        while cur is not node and is not None:
            prev = cur
            cur = cur.next
        
        if cur is None: #if you reach end of linked list without finding the target node
            return "Node not found."
        else:
            prev.next = cur.next #jump over the node to be deleted


class Hash_Table:
    def __init__(self, capacity):
        self.list = [None] * capacity
        self.size = 0
        self.capacity = capacity

    #function to create a hash code from key
    def _hash(self, key):
        return hash(key) % self.capacity #use python's inbuilt hashing function

    #function to insert new key value pair
    def insert(self, key, value):
        index = self._hash(key) #generate hash code

        if self.list[index] is None: #if nothing in index yet (can also thus assume key is not yet in hash table)
            new_link_list = Linked_List(new_node) #create new linked list
            self.list[index] = new_link_list #insert linked list at hashed index
        else:
            cur = self.list[index].head #else, if there is already at least one node at the index
            
            if cur.key == key: #if the head key is the same as the insert key
                cur.next.value = value #update value 
                return #immediately return
            
            #otherwise, if key not at head
            while cur.next.key != key and cur.next is not None: #traverse until you find the same key or until end of linked list
                cur = cur.next
            
            if cur.next is not None: #if key already exists somewhere in the list, but not at the head
                cur.next.value = value #update value
            else:
                new_node = Node(key, value) #create new node using key value pair
                cur.next = new_node #insert node

    #function to search for key value pair given the key
    def search(self, key):
        index = self._hash(key)

        if self.list[index] is None:
            return "Key not found."
        else:
            cur = self.list[index].head

            if cur.key == key: #if the searched key matches the head key
                return cur.value #immediately return the value

            #otherwise, if key not at head
            while cur.next.key != key and cur.next is not None: #traverse until you find the same key or until end of linked list
                cur = cur.next

            if cur.next is not None: #if key already exists somewhere in the list, but not at the head
                return cur.next.value #return value
            else:
                return "Key not found."

    #function to remove a key value pair given the key
    def remove(self, key):
        index = self._hash(key)

        if self.list[index] is None:
            return "Key not found."
        else:
            cur = self.list[index].head

            if cur.key == key: #if the searched key matches the head key
                temp_head = cur
                self.list[index].head = cur.next #set head to the second value in the linked list
                return temp_head #immediately return the deleted node

            #otherwise, if key not at head
            while cur.next.key != key and cur.next is not None: #traverse until you find the same key or until end of linked list
                cur = cur.next

            if cur.next is not None: #if key already exists somewhere in the list, but not at the head
                temp_cur_next = cur.next
                cur.next = cur.next.next #skip over the node with the key
                return temp_cur_next #return the removed node
            else:
                return "Key not found."
            