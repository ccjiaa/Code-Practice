class Linked_List:
    def __init__(self, head):
        self.head = head

    def append(self, node):
        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = node