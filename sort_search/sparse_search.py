def sparse_search(sparse_list, target):
    if target not in sparse_list:
        return -1
    
    return sparse_binary_search(sparse_list, 0, len(sparse_list) - 1, target, True)


#recursive method that conducts a binary search
def sparse_binary_search(arr, start, end, target, prev_mid):
    if start > end:
        return -1 #target not found
    
    #default keep decreasing mid until you find a non empty string, as in worse case the first value of the list will always be non-empty
    mid = (start + end)//2

    temp_mid = mid #set temp_mid to mid
    while arr[temp_mid] == "": #iterate down
        temp_mid -= 1
    
    #if you defaulted to the same midas the previous run, means you need to search in the other direction
    if temp_mid == prev_mid:
        temp_mid = mid #reset temp_mid to mid
        while arr[temp_mid] == "": #iterate up
            temp_mid += 1

    #set mid to temp_mid
    mid = temp_mid

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return sparse_binary_search(arr, start, mid, target, mid)
    else:
        return sparse_binary_search(arr, mid, end, target, mid)
    

#This is O(N) time, because it's binary search but in worse case you will need to traverse the entire list to find a valid mid value

spar_li = ["amber", "", "", "", "bennett", "chiori", "", "", "keqing", "", "", "", "mualani", "", ""]

print(sparse_search(spar_li, "bennett"))
print(sparse_search(spar_li, "keqing"))
print(sparse_search(spar_li, "jean"))