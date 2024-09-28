def peaks_and_valleys(list):
    list.sort()
    if len(list)%2 == 0: #if even
        mid = len(list)//2
    else: #if odd
        mid = len(list)//2 + 1
    start = 0 

    while mid < len(list) - 1:
        temp = list[start]
        list[start] = list[mid]
        list[mid] = temp

        start += 2
        mid += 2

    return list



li = [1, 7, 3, 6, 5, 6, 6, 10, 9, 1]

print(peaks_and_valleys(li))