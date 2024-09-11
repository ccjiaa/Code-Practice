class My_Queue:
    def __init__(self, value):
        self.stack_1 = []
        self.stack_2 = []

        self.stack_1.push(value)

    #Push is O(1) time so add is also
    def add(self, value):
        self.stack_1.push(value)
    
    #While this contains a while loop, it can be argued that since stack 1 is only emptied after long periods of time
    # the time is amortized and the resulting time is still about O(1)
    def remove(self):
        if self.stack_2.empty(): #if stack 2 is empty
            while self.stack_1.empty(): #while stack 1 is not empty
                temp_val = self.stack_1.pop() #pop off the top value of stack 1
                self.stack_2.push(temp_val) #push them to the bottom of stack 2 in reverse order
            
        return self.stack_2.pop()

    #Same logic as remove()
    def peek(self):
        if self.stack_2.empty(): #if stack 2 is empty
            while self.stack_1.empty(): #while stack 1 is not empty
                temp_val = self.stack_1.pop() #pop off the top value of stack 1
                self.stack_2.push(temp_val) #push them to the bottom of stack 2 in reverse order
            
        return self.stack_2.peek()
    
    #empty() is O(1) time therefore is_empty is also O(1) time
    def is_empty(self):
        if self.stack_1.empty() and self.stack_2.empty():
            return True
        return False