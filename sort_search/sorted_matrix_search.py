def sorted_matrix_search(mat, target):
    list_idx = binary_search(mat, 0, len(mat) - 1, target, True) #binary search returns the list that contains the range of values that may contain target
    list = mat[list_idx]

    col_idx = binary_search(list, 0, len(list) - 1, target, False)
    
    new_tuple = (list_idx, col_idx)

    return new_tuple

#recursive method that conducts a binary search
def binary_search(arr, start, end, target, is_matrix):
    if is_matrix:
        if start == end:
            return start #return when narrow matrix down to one list
    else:
        if start > end:
            return -1 #target not found
    
    mid = (start + end)//2

    #if matrix, compare to first value of each list
    if is_matrix:
        if arr[mid][0] <= target and arr[mid][len(arr[mid]) - 1] >= target:
            return mid
        elif arr[mid][0] > target:
            return binary_search(arr, start, mid, target, True)
        else:
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
       [4, 5, 6],
       [7, 8, 9]]

print(sorted_matrix_search(mat, 6))