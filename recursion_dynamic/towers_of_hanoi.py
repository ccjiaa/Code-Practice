def towers_of_hanoi(stack):
    transition = []
    goal = []

    transfer_disks(len(stack), stack, transition, goal)

    return goal


def transfer_disks(stack_size, stack, transition, goal):
    if stack_size < 2: #if only one value in stack, immediately transfer from stack to goal
        goal.append(stack.pop())
        return
    if stack_size < 3:
        #print_hanoi(stack, transition, goal)
        transition.append(stack.pop())
        #print_hanoi(stack, transition, goal)
        goal.append(stack.pop())
        #print_hanoi(stack, transition, goal)
        goal.append(transition.pop())
        return

    transfer_disks(stack_size - 1, stack, transition, goal)
    transition.append(stack.pop())
    transfer_disks(stack_size - 1, goal, transition, stack)
    goal.append(transition.pop())
    transfer_disks(stack_size - 1, stack, transition, goal)


def print_hanoi(stack, transition, goal):
    print(stack)
    print(transition)
    print(goal)
    print(" ")


#Please uncomment the print_hanoi calls in transfer_disks to verify that smaller values are never below larger ones
#Idea: repeatedly run transfer disks back and forth, adding one more larger disk each time, until all disks are in goal
#      because we start with the smallest disks, we are essentially "ignoring" the larger disks at the bottom of the starting stack
#      (as if they weren't there). We can do this because the smaller disks are always smaller than the next larger disk, so the
#      larger disks are irrelevant
#This is O(3^N) time, because each call of transfer_disks calls itself 3 times, and thus creates 3 branches with N layers

stac = [4, 3, 2, 1]
print(towers_of_hanoi(stac))