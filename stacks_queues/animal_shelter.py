#Class to create new nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#Class to create new linked list
class Linked_List:
    def __init__(self, head):
        self.head = head

    def append(self, node):
        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = node


#Class to create new animal shelter
class Animal_Shelter:
    def __init__(self):
        self.shelter_link = Linked_List(None)
        self.cat_link = Linked_List(None)
        self.dog_link = Linked_List(None)

        self.shelter_link.append(self.cat_link)
        self.shelter_link.append(self.dog_link)

        self.order = 0

    def enqueue(self, animal, type): #type -> cat = "cat", dog = "dog"
        self.order += 1
        new_tup = (animal, self.order) #create a tuple marking the animal and its order, (string, int)

        if type == "cat":
            curr = self.cat_link.head #set iterating node to start in cat link list
            temp_list = self.cat_link #store linked list
        else:
            curr = self.dog_link.head #set iterating node to start in dog link list
            temp_list = self.dog_link #store linked list

        if curr == None:
            temp_list.head = Node(new_tup) #if link list empty, add this animal as head
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(new_tup)

    def dequeue_any(self):
        if self.shelter_link.head is None:
            return "Sorry, the shelter is empty!"
        
        cat_head = self.shelter_link.head.head
        dog_head = self.shelter_link.head.next.head
        
        if cat_head is None and dog_head is not None: #if there are no cats but there are dogs
            self.dequeue_dog() #dequeue one dog
        
        elif cat_head is not None and dog_head is None: #if there are cats but there are no dogs
            self.dequeue_cat() #dequeue one cat
        
        else: #if there are both dogs and cats
            if cat_head.data[1] < dog_head.data[1]: #if the order of the cat link head is smaller than the order of the dog link head
                self.dequeue_cat()
            else:
                self.dequeue_dog()
    
    def dequeue_dog(self):
        temp_head = self.dog_link.head #store the current head node
        self.dog_link.head = temp_head.next #cut off current head node

        return temp_head.data[0] #return dog
    
    def dequeue_cat(self):
        temp_head = self.cat_link.head #store the current head node
        self.cat_link.head = temp_head.next #cut off current head node

        return temp_head.data[0] #return cat

#Only potential problem is that order will keep increasing and will eventually integer overflow. 

sunrise = Animal_Shelter()
sunrise.enqueue("potato", "dog")
sunrise.enqueue("tomato", "cat")
sunrise.enqueue("ice cream", "dog")

print(sunrise.dequeue_any())