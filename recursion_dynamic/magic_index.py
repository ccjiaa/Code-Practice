def magic_index(list):
    return magic_binary_search(list, 0, len(list) - 1) #initialize the recursion

def magic_binary_search(list, start, end):
    if start > end: #break when start exceeds end, return -1 for no value found (index is non-negative)
        return -1
    mid = (start + end)//2 #find middle

    if list[mid] == mid: #if mid is a magic number, return
        return mid
    elif list[mid] < mid: #else if the value at mid is lower than the index
        return magic_binary_search(list, start, mid) #check lower
    else:
        return magic_binary_search(list, mid + 1, end) #else check higher
    

#This is O(log(N)), since it's essentially a modified binary search
#However, the modification is just a change to the conditional, so time doesn't change
#Thus this is still O(log(N)) time

li = [3, 6, 7, 8, 8, 8, 8, 8, 8]
lis = [3, 3, 6, 7, 8, 9, 10]
print(magic_index(li))
print(magic_index(lis))