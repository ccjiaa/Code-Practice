def validate_bst(tree):
    root = tree.head_list[0]

    #Default assume two children exist
    is_right = True
    is_left = True

    #If no children, immediately return True, since parent must be True to arrive to the child
    if len(root.child_list) < 1:
        return True
    #Else if 1 child, compare child value to parent value to determine if left or right child, set the other flag to False
    elif len(root.child_list) == 1:
        is_single_child = True
        if root.child_list[0] <= root.data:
            is_right = False
        else:
            is_left = False
    
    pos_inf = float('inf')
    neg_inf = float('-inf')

    is_search_tree_list = [True]

    if is_right:
        if is_single_child:
            validate_node(root.child_list[0], pos_inf, root.data, is_search_tree_list)
        else:
            validate_node(root.child_list[1], pos_inf, root.data, is_search_tree_list)
    
    if is_left:
        validate_node(root.child_list[0], root.data, neg_inf, is_search_tree_list)

    return is_search_tree_list[0]



def validate_node(node, max, min, is_search_tree_list):
    #If tree is already proven to not be BST from elsewhere, then immediately return False
    if not is_search_tree_list[0]:
        return False
    
    #Default assume two children exist
    is_right = True
    is_left = True
    is_single_child = False

    #If no children, immediately return True, since parent must be True to arrive to the child
    if len(node.child_list) < 1:
        return True
    #Else if 1 child, compare child value to parent value to determine if left or right child, set the other flag to False
    elif len(node.child_list) == 1:
        is_single_child = True
        if node.child_list[0] <= node.data:
            is_right = False
        else:
            is_left = False

    #If right child exists
    if is_right:

        #Create variable for the child node for easier use
        if is_single_child:
            child_right = node.child_list[0]
        else:
            child_right = node.child_list[1]

        #If the node is to the right of the root node/grandparent node, but to the left of its parent node, it must be greater than the root (min) and less than the parent (node.data)
        #Vice-versa for when the node is to the left of the root node/grandparent node, but to the right of the parent node (node.data)
        #If the node is to the left of the root node and to the left of its parent, it needs only be less than its parent since its parent must be less than the root
        #Likewise, if the node to the right of the root and right of its parent, then it needs only be greater than its parent since its parent must already be less than the root
        #Once the list chances to False, any future recursive calls will immediately return preventing unnecessary work
        if child_right.data > max or child_right.data < node.data:
            is_search_tree_list[0] = False
            return False
        
        #When moving right in the tree, only the minimum is affected, and updated to the parent node
        bool_right = validate_node(child_right, max, node.data, is_search_tree_list)

        #If child returned False, pass it up along the recursion
        if not bool_right:
            return False

    #If left child exists
    if is_left:
        child_left = node.child_list[0]
        
        if child_left.data < min or child_left.data > node.data:
            is_search_tree_list[0] = False
            return False
    
        #When moving left in the tree, only the maximum is affected, and updated to the parent node
        bool_left = validate_node(node.child_list[0], node.data, min, is_search_tree_list)

        if not bool_left:
            return False
    
    #If never proven False, must be True
    return True
