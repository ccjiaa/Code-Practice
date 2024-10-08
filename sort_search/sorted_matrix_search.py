def sorted_matrix_search(mat, target):
    list_idx = binary_search(mat, 0, len(mat) - 1, target, True) #binary search returns the list that contains the range of values that may contain target
    
    #if target not in the range of the columns, immediately return -1
    if list_idx == -1:
        return -1
    
    list = mat[list_idx]

    col_idx = binary_search(list, 0, len(list) - 1, target, False) #find the colo

    #if not in the chosen list, immediately return -1
    if col_idx == -1:
        return -1
    
    new_tuple = (list_idx, col_idx) #add indexes into a tuple like a coordinate

    return new_tuple

#recursive method that conducts a binary search
def binary_search(arr, start, end, target, is_matrix):
    if is_matrix:
        if start >= end:
            return -1 #target range not found
    else:
        if start >= end:
            return -1 #target not found
    
    mid = (start + end)//2

    #if matrix, compare to first value of each list
    if is_matrix:
        if arr[mid][0] <= target and arr[mid][len(arr[mid]) - 1] >= target: #if you are within range of the list in mid
            return mid
        elif arr[mid][0] > target: #if less than the mid list's range, search below
            return binary_search(arr, start, mid, target, True)
        else: #else, search above
            return binary_search(arr, mid + 1, end, target, True)
    else: #else do normal list binary search
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, start, mid, target, False)
        else:
            return binary_search(arr, mid + 1, end, target, False)
        
    
#This is O(Mlog(M) + Nlog(N)) time, since it's a binary search in the rows followed by a binary since in the columns 


mat = [[1, 2, 3],
       [4, 6, 6],
       [7, 8, 9]]

print(sorted_matrix_search(mat, 5))