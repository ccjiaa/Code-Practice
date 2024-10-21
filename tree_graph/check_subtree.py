def check_subtree(big_tree_root, small_tree_root):
    node_list = []
    find_same_node_value(node_list, small_tree_root.data, big_tree_root) #find all potential matching nodes for the subtree

    for big_root in node_list: #for every potential small_tree start in the big_tree
        is_sub = [True] #reset is_sub to true
        check_same_tree(big_root, small_tree_root, is_sub) #check if it's the same
        if is_sub[0]: #if traveled through the entirety of the two trees without is_sub turning false, small tree is subtree
             return True
    
    return False #if never true, must be false


def check_same_tree(root1, root2, is_sub):
        if not is_sub[0]: #if confirms not subtree, return immediately
             return
        if root1.data != root2.data: #if node values differ, not subtree, set is_sub to false and immediately return
            is_sub[0] = False
            return
        if root1 is None and root2 is None: #if both nodes are None, return to continue pre-order traversal
            return

        #Repeat for both child branches in pre-order traversal
        check_same_tree(root1.left, root2.left)
        check_same_tree(root1.right, root2.right)


#Method to find all nodes with the same value as value
def find_same_node_value(node_list, value, search_node):
    if search_node is None: #if you reach the end, return
        return
    if search_node.value == value: #if you find a node with the same value, add it to the list of potential starting nodes
        node_list.append(search_node)

    #check both children
    find_same_node_value(node_list, value, search_node.left)
    find_same_node_value(node_list, value, search_node.right)

    return