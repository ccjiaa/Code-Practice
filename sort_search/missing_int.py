#int takes up at most 4 bytes. 
#Because we have 4 billion ints, we need at most 16 billion bytes of memory is we wanted to use merge sort
#But, 16 billion bytes is 16 gigabytes, and we are only given 1 gigabyte of memory
#Thus, we use quick sort

def partition(list, low, high):
    pivot = high
    i = low - 1
    
    for k in range(low, high):
        if list[k] < pivot: #if smaller than pivot
            i += 1 #increase i index to next index

            #swap smaller k index value with whatever is at i index
            temp = list[i]
            list[i] = list[k]
            list[k] = temp
    
    #move pivot to the spot after the last smaller value
    temp_two = list[i + 1]
    list[i + 1] = list[high]
    list[high] = temp_two

    return i + 1 #returns position of pivot 


def quick_sort(list, low, high):
    if low > high:
        return
    
    pivot_idx = partition(list, low, high)

    quick_sort(list, low, pivot_idx - 1)
    quick_sort(list, pivot_idx + 1, high)


def missing_int(list):
    quick_sort(list, 0, len(list) - 1) #quick sort in ascending order

    return list[-1] + 1 #return last and largest value in the list, plus 1, which is guaranteed to not be in the original list


#This is O(Nlog(N)) time, since quick sort is O(Nlog(N)) time and the final return addition is constant time, which is absorbed. 


li = [1, 5, 8, 2, 4, 6, 4, 5]
print(missing_int(li))