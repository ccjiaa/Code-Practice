def permutation(str):
    str_list = [] #initialize list to hold subsets
    return permute(str, str_list) #initialize recursion

def permute(str, str_list):
    if len(str) < 2: #if only one letter, immediately return
        return str
    if len(str) < 3: #if two letters, swap their places and append the swapped and original
        str_list.append(str)
        reverse_str = str[1] + str[0]
        str_list.append(reverse_str)
        return str_list
    
    smaller_str = str[:-1] #get rid of the rightmost (last) letter in the larger str
    str_list = permute(smaller_str, str_list) #find all permutations of the smaller str
    pass_list = [] #create a list to hold the permutations of the larger str (str)
    new_letter = str[-1:] #save the value of the last letter
    temp_dict = {} #create dict to check for duplicates later

    for i in range(len(str_list)): #iterate through the smaller string subset list
        temp_str = str_list[i] #create a temporary str to modify it
        for k in range(len(str_list[i]) + 1): #iterate through each position in the permutations of the smaller str, including in front and in back
            #split the string in half
            str_front = temp_str[:k]
            str_back = temp_str[k:]
            new_str = str_front + new_letter + str_back
            if new_str in temp_dict:
                continue
            else:
                temp_dict[new_str] = 1
                pass_list.append(str_front + new_letter + str_back) #append string with the new_letter inserted
    
    return pass_list #return upwards to previous recursive call


#This is O(N * N! * N^2), which simplifies to O(N!). 
# Same as the no dupes version. The dict only changes space complexity (for the worse). We stil do the same amount of work per recursive cycle
#Note: as the without dupes version of big O explanation is kind of bs, this will also be returned to at a later date
print(permutation("rrd"))
#red -> red, rde, erd, edr, dre, der