def group_anagrams(list):
    if len(list) < 3:
        return list
    
    list.sort() #sort list in order of string length (problem is here, list,sort() only sorts alphabetically, ignores string length)

    print(list)

    temp_mat = [[]]

    cur_len = letter_count(list[0]) #current length category starts at length of smallest string
    mat_idx = 0 #index of the matrix

    
    #put each length category into their own list in a matrix
    for str in list:
        length = letter_count(str) #get length
        if length > cur_len: #if new length category
            temp_mat.append([]) #append a new list
            mat_idx += 1 #increase matrix index

        temp_mat[mat_idx].append(str) #append str to the current length category list

    for list in temp_mat: #repeat for all count categories

        for i in range (len(list) - 2): #stop at the SECOND last value in the list
            base_str_list = convert_to_list(list[i])
            base_str_list = delete_spaces(base_str_list) #transform base string into a list with no spaces
            base_str_list.sort() #sort in ascending alphabetical order

            for k in range(i, len(list) - 1): #start at current base string, iterate until at SECOND last value in the list
                compare_list = convert_to_list(list[k + 1])
                compare_list = delete_spaces(compare_list) #transform next string in list to a list
                compare_list.sort() #sort in ascending alphabetical order

                print(compare_list == base_str_list)

                if compare_list == base_str_list: #if compare list identical to base list, anagram
                    temp = list[i + 1] #save value of value after the base value
                    list[i + 1] = list[k + 1] #set value after base to the anagram
                    list[k + 1] = temp #swap
                    i += 1 #iterate i to move base value forward for next outer for loop iteration, since anagrams contain same letters, so anagram of anagram is also anagram of original base
    
    new_list = []
    for list in temp_mat:
        new_list = new_list + list
    
    return new_list



def letter_count(str):
    count = 0
    for letter in str:
        if letter != " ":
            count += 1

    return count

def convert_to_list(str):
    new_list = []
    for letter in str:
        new_list.append(letter)
    
    return new_list

def delete_spaces(list):
    for i in range(len(list) - 1):
        if list[i] == " ":
            list.pop(i)

    return list

li = ["potato", "smash", "tapoto"]
group_anagrams(li)
print(li)