class Three_In_One:
    def __init__(self, idx_x, idx_y, idx_z, val_x, val_y, val_z):
        self.idx_x = idx_x
        self.idx_y = idx_y
        self.idx_z = idx_z

        self.idx_end_y = 1

        self.val_x = val_x
        self.val_y = val_y
        self.val_z = val_z

        self.stack = [val_x, val_y, val_z]

    #Potential problem: insert is O(N) time, but stack push needs to be O(1) time...
    def push(self, chosen_stack, data):
        stack_idx = -1
        if chosen_stack == "1":
            stack_idx = self.idx_x
            self.idx_y += 1 #adding to the beginning of x pushes beginning of y and z down
            self.idx_z += 1
            self.idx_end_y += 1 #index of end of stack 2
        elif chosen_stack == "2":
            stack_idx = self.idx_y
            self.idx_z += 1 #adding to the beginning of y pushes beginning of z down
            self.idx_end_y += 1 
        else:
            stack_idx = self.idx_z #adding to the beginning of z doesn't affect the start of x or y
            self.idx_end += 1 

        self.stack.insert(stack_idx)

    #List pop is apparently O(1), so this should also be O(1)
    def pop(self, chosen_stack):
        stack_idx = -1
        if chosen_stack == "1":
            stack_idx = self.idx_x
            if self.idx_x == self.idx_y: #if start of first and second indexes are the same, then first must be empty, second may be empty
                return "Stack empty"
            self.idx_y -= 1 #adding to the beginning of x pushes beginning of y and z down
            self.idx_z -= 1
            self.idx_end -= 1 #index of end of stack 2
        elif chosen_stack == "2":
            stack_idx = self.idx_y
            if self.idx_y == self.idx_z: #if start of second and third indexes are the same, then second must be empty
                return "Stack empty"
            self.idx_z -= 1 #adding to the beginning of y pushes beginning of z down
            self.idx_end -= 1
        else:
            stack_idx = self.idx_z #adding to the beginning of z doesn't affect the start of x or y
            if self.idx_end_y == self.idx_z:
                return "Stack empty"
            self.idx_end -= 1

        self.stack.pop(stack_idx)

    def is_empty(self):
        if self.idx_x == self.idx_y and self.idx_y == self.idx_z == self.index_end_y:
            return True
        return False