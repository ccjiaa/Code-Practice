def sort_search_no_size(listy, target):
    #check if first value in listy is target, because we start calc0ing length at index = 1
    if listy[0] == target:
        return 0
    
    #double potential length until you are out of range
    length_idx = 1
    while listy[length_idx] != -1:
        length_idx *= 2
    
    #decrease by 1 until you reach the end of the listy
    while listy[length_idx] == -1:
        length_idx -= 1

    #do binary search
    return binary_search(listy, 0, length_idx, target)

#recursive method that conducts a binary search
def binary_search(arr, start, end, target):
    if start > end:
        return -1 #target not found
    
    mid = (start + end)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, start, mid, target)
    else:
        return binary_search(arr, mid + 1, end, target)
    

#This solution is O(log(N)) time
#Finding the length of the listy takes O(log(N)) time, since we increase the potential length exponentially
#Binary search is also O(log(N)) time, thus both add up to O(log(N)) time

#Note: Not yet tested due to take to create a new class to avoid the index out of range error that the provided listy class has

li = [1, 3, 4, 5, 7, 9, 10]

print(sort_search_no_size(li, 7))