#Here, it will be assumed that the node class contains both a list of children as well as a variable containing its parent node

def successor(node):
    parent = node.parent

    #Unique case for when node is the root of the tree
    if parent is None: #if root
        if len(node.child_list) < 1: #if no children
            return None #no next node
        
        elif len(node.child_list) == 1: #if one child
            if is_right_child(node.child_list[0]): #if right child, return as next
                return node.child_list[0]
            else: #else if left child, root is the rightmost (last) node, no next node
                return None
            
        else: #two children
            if is_right_child(node.child_list[0]): #if first child in list is right child
                return node.child_list[0] #return it as next node
            else: #else second child must be right child
                return node.child_list[1] #return it as next node

    #General case
    if len(node.child_list) < 1: #if current node has no children
        if is_right_child(node): #if current node is the right child
            temp_node = node
            while is_right_child(temp_node): #keep iterating through parents until the temp_node is a left child or root
                if temp_node.parent is None: #if current node is the root node, original node was rightmost node of the tree, no next node
                    return None
                temp_node = temp_node.parent
            return temp_node.parent #else, when the temp_node is the left child, return its parent as the next node
        else: #must be left node
            return node.parent #found left child, immediately return parent as next node
        
    elif len(node.child_list) == 1: #else if one child
        if is_right_child(node.child_list[0]): #if child is right child
            return node.child_list[0] #return the right child as next node
        else: #else if only left child available, current node is rightmost, next node must be parent
            return node.parent
            
    else: #else two children
        if is_right_child(node.child_list[0]): #if first child in list is right child
                return node.child_list[0] #return it as next node
        else: #else second child must be right child
            return node.child_list[1] #return it as next node


#Method to check if input node is the right child of its parent
def is_right_child(node):
    if node.data > node.parent.data:
        return True

    return False