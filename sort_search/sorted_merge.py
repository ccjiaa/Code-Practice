def sorted_merge(list_a, list_b):
    if len(list_a) < 1 and len(list_b) < 1: #if both lists empty
        return None
    elif len(list_a) < 1: #if list a empty
        return list_b
    elif len(list_b) < 1: #if list b empty
        return list_a
    else: #else, if both are NOT empty
        for value in list_b:
            index_a = len(list_a) - 1 #go to last item in list a
            while index_a >= 0: #iterate through list a
                if value <= list_a[index_a]: #if value from list b is smaller
                    list_a.insert(index_a, value) #insert in that spot in list a
                    break
                index_a -= 1 #iterate index

            if index_a < 0: #if iterated through entire list
                list_a.append(value) #know value is larger than all values in list a, append to end

        return list_a
    
li = [1, 4, 9]
lis = [2, 8, 9, 10]

print(sorted_merge(li, lis))