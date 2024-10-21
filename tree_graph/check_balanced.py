#1. recusive
#2. find depth, mark depth of each subtree as you go along
#3. now when you get to that subtree in the future, you'll already know its depth?
#4. What??

#Alt
#1. iterative
#2. DFS, get to bottom of leftmost
#3. Note the depth in a dict, check if the depth += 2 is also in the dict
#4. If yes, return False immediately since you have depth difference >2, else continue
#5. Now just keep iterating to the side
#6. If you iterate through the entire tree without finding a depth diff >2, return True

from collections import deque
from Graph import Graph
from Graph_Node import Graph_Node

def check_balanced(tree):
    #Get the root node
    root = tree.head_list[0]

    #Create a list with only one boolean value. This value will be changed in real time to minimize unnecessary work
    is_balanced_list = [True]

    #Create a dict to hold the lengths of the branches
    len_dict = {}

    #Initiate recursion
    is_sub_balanced(root, 1, len_dict, is_balanced_list)

    return is_balanced_list[0]


def is_sub_balanced(node, cur_depth, len_dict, is_balanced_list):
    #Increase depth by 1
    cur_depth += 1

    #If no children
    if len(node.child_list) < 1: 

        #If there are existing branches that differ in length by more than 1, not balanced binary tree
        if (cur_depth - 2) in len_dict or (cur_depth + 2) in len_dict:
            is_balanced_list[0] = False
        
        #Otherwise, add the length to the dict. No need to increment since we only care that it's in the dict
        elif cur_depth not in len_dict:
            len_dict[cur_depth] = 1

        #Immediately return to not do unnecessary work
        return

    #Updates in real time due to being a list. If another branch already breaks the balance, immediately return
    if not is_balanced_list[0]:
        return
    else:
        #Otherwise, call self on both child node branches
        is_sub_balanced(node.child_list[0], cur_depth, len_dict, is_balanced_list)
        is_sub_balanced(node.child_list[1], cur_depth, len_dict, is_balanced_list)

    return