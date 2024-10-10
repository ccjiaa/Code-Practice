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

    for i in range(len(str_list)): #iterate through the smaller string subset list
        temp_str = str_list[i] #create a temporary str to modify it
        for k in range(len(str_list[i]) + 1): #iterate through each position in the permutations of the smaller str, including in front and in back
            #split the string in half
            str_front = temp_str[:k]
            str_back = temp_str[k:]

            pass_list.append(str_front + new_letter + str_back) #append string with the new_letter inserted
    
    return pass_list #return upwards to previous recursive call


#Note: there should always be n! permutations, where n is the length of the string
#This is O(N * N! * N^2), which simplifies to O(N!).
#The N is from the linear recursion, since each run only calls itself once, so one branch
#The N! comes from the outer for loop, since you will do N! every call of the recursive function
#   e.g. once the 1st run, twice the 2nd, 6 times the 3rd, 24 times the 4th, etc
#The N^2 comes from the summation from 0 to N because equal to N^2 in big O, and we do 0 to N amount of work per loop
#In all three cases, N is the length of the string being permuted
#Note: this big O explanation is kind of bs, will come back to it at a later date

print(permutation("rrd"))
#red -> red, rde, erd, edr, dre, der