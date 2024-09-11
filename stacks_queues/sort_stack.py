class sort_stack:
    def __init__(self, value):
        self.stack = [value]

    def push(self, value):
        temp_top = self.stack.peek()
        temp_stack = []

        while temp_top < value:
            temp_pop = self.stack.pop() #pop off the top item
            temp_stack.push(temp_pop)   #place it in a temporary stack
            temp_top = self.stack.peek() #check the next value

        self.stack.push(value)

        while not temp_stack.empty(): #while temporary stack isn't empty
            self.stack.push(temp_stack.pop()) #pop values from temp_stack, push back into main stack

    #just the normal stack pop
    def pop(self):
        return self.stack.pop()

    #normal peek
    def peek(self):
        return self.stack.peek()

    #normal empty
    def empty(self):
        return self.stack.empty()

#This is really inefficient since this is basically insertion sort