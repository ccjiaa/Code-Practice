def search_rotated_array(rot_arr, target):

    #find location of pivot
    pivot_idx = 0
    for i in range(1, len(rot_arr) - 1):
        if rot_arr[i] < rot_arr[pivot_idx]:
            break
        pivot_idx = i

    if rot_arr[pivot_idx] == target: #if pivot is target, return pivot
        return pivot_idx
    elif target >= rot_arr[0]: #else if target is larger than the looped back part
        if target == rot_arr[0]: #if equal, return 0 immediately
            return 0
        else:
            return binary_search(rot_arr, 0, pivot_idx, target) #else, do binary search on the looped portion of the array
    else: #otherwise, if less than the looped back part
        if target == rot_arr[len(rot_arr) - 1]: #if equal to the last non-looped back value, return immediately
            return len(rot_arr) - 1 
        else:
            return binary_search(rot_arr, pivot_idx + 1, len(rot_arr) - 1, target) #else, do binary search on the non-looped portion of the array


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
    
#This solution is O(N) time. Searching for the pivot takes O(N) time, since a non-rotated array will cause the method to iterate through the entire array
#the binary search portion is O(log(N)) time, and is thus absorbed by the O(N) time used to find the pivot
#As a result, the final time complexity is O(N) time

li = [5, 6, 7, 8, 1, 2, 3, 4]

print(search_rotated_array(li, 3))