def path_with_sums(root, sum):
    if root.data == sum:
        return 1
    
    return path_with_sums_helper(root.left, root.data, sum) + path_with_sums_helper(root.right, root.data, sum)


def path_with_sums_helper(cur_node, cur_sum, target_sum):
    if cur_node is None: #if node is none, reached the end of the branch, return 0 ways
        return 0
    
    new_sum = cur_node.data + cur_sum

    if new_sum == target_sum: #if equal to the sum, return 1 way + any others further down the paths
        return 1 + path_with_sums_helper(cur_node.left, new_sum, target_sum) + path_with_sums_helper(cur_node.right, new_sum, target_sum) #add number of ways from left and right paths

    return path_with_sums_helper(cur_node.left, new_sum, target_sum) + path_with_sums_helper(cur_node.right, new_sum, target_sum) #add number of ways from left and right paths


#This should be O(N) time where N is the number of nodes, since this program touches each node once and does constant work on each node