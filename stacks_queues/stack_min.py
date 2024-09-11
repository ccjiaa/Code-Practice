class Stack_Min:
    def __init__(self, value):
        self.stack = []
        value_min_tuple = (value, value) #tuple with the following parameters: (value, min value of all values below)
        self.stack.push(value_min_tuple)

    #Peek and push are both O(1) time, therefore this push is also O(1) time
    def push_min_ver(self, value):
        min_val_below = self.stack.peek()[1] #get min value of all values below this one

        val_min_tup = (value, self.stack.peek()[1])
        if min_val_below < value:
            val_min_tup = (value, min_val_below)
        else:
            val_min_tup = (value, value)

        self.stack.push(val_min_tup)

    #Pop is O(1) time therefore this pop is also O(1) time
    def pop_min_ver(self):
        return self.stack.pop()[0]
    
    #Peek is O(1) time therefore min is as well
    #Minimum values of all elements below current element is stored in the element, so we just need to peek it
    def min(self):
        return self.stack.peek()[1]