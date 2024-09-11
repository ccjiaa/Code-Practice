class Set_Of_Stacks:
    def __init__(self, value, threshold): #assume threshold > 0
        self.threshold = threshold
        self.stack_list = []

        start_stack = []
        start_stack.push(value)

        stack_tuple = (start_stack, 1) #contains stack and stack size

        self.stack_list.append(stack_tuple)

    def push(self, value):
        if self.stack_list[-1][1] < self.threshold:
            self.stack_list[-1][0].push(value) #push to the last stack in the tuple in the list
            self.stack_list[-1][1] += 1 #increment the length
        else:
            new_stack = [value]
            new_tup = (new_stack, 1) #create a new stack length tuple
            self.stack_list.append(new_tup) #add new stack tuple pair to the stack list

    def pop(self):
        self.stack_list[-1][0].pop() #pop topmost item from last stack
        if self.stack_list[-1][0].empty():
            self.stack_list.pop() #delete the empty stack
        else:
            self.stack_list[-1][1] -= 1 #reduce length of popped stack by 1 if not empty

    def pop_at(self, index):
        self.stack_list[index][0].pop() #pop topmost item from the stack at index index
        if self.stack_list[index][0].empty():
            self.stack_list.pop() #delete the empty stack
        else:
            self.stack_list[index][1] -= 1 #reduce length of popped stack by 1 if not empty

#Note: Could possibly just use len to check length, but just in case, use tuple