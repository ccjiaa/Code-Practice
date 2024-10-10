import copy

class Box:
    def __init__(self, h, w, d):
        self.height = h
        self.width = w
        self.depth = d

def stacks_of_boxes(box_list):
    # You can implement functionality here, possibly calling quick_sort
    quick_sort(box_list, 0, len(box_list) - 1)
    return box_list

def quick_sort(box_list, low, high):
    # Return after quick-sorting everything in the list
    if low < high:
        # Save index of pivot after partition
        pivot_idx = partition(box_list, low, high)

        # Do quick_sort before and after the pivot
        quick_sort(box_list, low, pivot_idx - 1)
        quick_sort(box_list, pivot_idx + 1, high)

def partition(box_list, low, high):
    # Choose last element as pivot
    pivot = box_list[high].height
    
    i = low - 1  # Initialize variable to traverse through insertion of the list

    for j in range(low, high):
        # Determine which of height, width, depth is being measured
        measurement = box_list[j].height

        # If element height less than pivot, place left of pivot
        if measurement >= pivot:
            i += 1
            # Swap elements
            box_list[i], box_list[j] = box_list[j], box_list[i]

    # Insert pivot after last element that is <= to itself
    i += 1
    box_list[i], box_list[high] = box_list[high], box_list[i]

    return i  # Return index after pivot

# Example usage
boxes = [Box(3, 2, 1), Box(1, 2, 3), Box(4, 5, 6)]
sorted_boxes = stacks_of_boxes(boxes)
for box in sorted_boxes:
    print(box.height, box.width, box.depth)


box_list = []

box_list.append(Box(1, 2, 3))
box_list.append(Box(4, 5, 6))
box_list.append(Box(2, 2, 4))
box_list.append(Box(5, 6, 5))
box_list.append(Box(1, 1, 1))


quick_sort(box_list, 0, 4)
print("sorted")
for box in box_list:
    print(box.height)


#sorting complete, come back to finish later once answer is less fresh in mind