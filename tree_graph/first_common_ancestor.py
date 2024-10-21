#Post-answer version

def first_common_ancestor(root, node1, node2):
    return

def first_common_ancestor_helper(root, node1, node2):
    if root is None or root is node1 or root is node2: #if you reach the end of the tree or find one of the target nodes first
        return root #last common ancestor is the root itself
    
    is_node1_left = is_in_subtree(root.left, node1)
    is_node2_left = is_in_subtree(root.left, node2)
    if is_node1_left != is_node2_left: #if two nodes aren't in the same subtree, return root as ancestor
        return root
    else: #else if they are on the same side
        if is_node1_left: #if they are both in the left subtree, search left subtree
            return first_common_ancestor_helper(root.left, node1, node2)
        else: #otherwise search right subtree
            return first_common_ancestor_helper(root.right, node1, node2)
        
    

#Note: This will run into index out of range errors due to using Graph.py for a binary tree
#In a specific binary tree object, we could specify that there's only a left child and right child, with any empty children being None
def is_in_subtree(root, target_node):
    if root is None: #if reach end of branch, then not in that specific branch
        return False
    if root is target_node: #if root is the node, return True for found
        return True

    return is_in_subtree(root.left, target_node) or is_in_subtree(root.right, target_node) #check both child branches, if found in neither then not in subtree








#Pre-answer version

# def first_common_ancestor(root, node1, node2):
#     is_node1 = [False]
#     is_node2 = [False]
#     if len(root.child_list) < 1 and ( root is not node1 or root is not node2 ):
#         return None
#     else:
#         root = root.child_list[0]
#         while len(root.child_list) < 2: #keep going until you reach the target nodes or a node with 2 children
#             if root is node1 or root is node2: #assuming that both node1 and node2 are in the tree, the first instance of either in a singly linked tree is the ancestor
#                 return root
#             root = root.child_list[0]

#     cur_ancestor = root
#     is_left = find_in_subtree(root.child_list[0], node1, is_node1, node2, is_node2)
#     is_right = find_in_subtree(root.child_list[1], node1, is_node1, node2, is_node2)
#     while ( is_left or is_right ) and len(root.child_list) > 0:
#         if len(root.child_list) == 2:
#             is_right = find_in_subtree(root.child_list[1], node1, is_node1, node2, is_node2)
#         is_left = find_in_subtree(root.child_list[0], node1, is_node1, node2, is_node2)

#         if is_right

# def find_in_subtree(sub_root, node1, is_node1, node2, is_node2):
#     if is_node1[0] and is_node2[0]: #if both nodes found return immediately
#         return
    
#     #Check if current root node is either of the target nodes
#     if sub_root is node1:
#         is_node1[0] = [True]
#     if sub_root is node2:
#         is_node2[0] = [True]

#     if len(sub_root.child_list) < 1: #if no children, end of tree
#         return
#     if len(sub_root.child_list) == 1:
#         find_in_subtree(sub_root.child_list[0], node1, is_node1, node2, is_node2)
#     else: #must be two children since binary tree
#         find_in_subtree(sub_root.child_list[0], node1, is_node1, node2, is_node2)
#         find_in_subtree(sub_root.child_list[1], node1, is_node1, node2, is_node2)

        
# #give, pls try again tomorrow ty