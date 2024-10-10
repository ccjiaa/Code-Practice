def parens(num):
    if num < 1:
        return [None]
    return generate_parens(num)


def generate_parens(num):
    if num < 2:
        temp_list = []
        temp_list.append("()")
        return temp_list
    if num < 3:
        temp_list = []
        temp_list.append("()()")
        temp_list.append("(())")
        return temp_list

    smaller_list = generate_parens(num - 1)
    wrap_list = smaller_list.copy()
    insert_list = []
    temp_dict = {}

    #surround all the pairings from the smaller list by parenthesis
    for i in range(len(smaller_list)):
        new_str = "(" + wrap_list[i] + ")"
        wrap_list[i] = new_str
        temp_dict[new_str] = 1

    for k in range(len(smaller_list)):
        temp_str = smaller_list[k]
        for m in range(len(temp_str)): #iterate through each position in the permutations of the smaller str, including in front and in back
            #split the string in half
            str_front = temp_str[:m]
            str_back = temp_str[m:]

            new_str = str_front + "()" + str_back

            if new_str in temp_dict: #if in hash table, skip
                continue
            else:
                temp_dict[new_str] = 1
                insert_list.append(new_str) #append string with the new_letter inserted

    return wrap_list + insert_list


#Alternative method: Inserting a "(" then inserting a ")" at increasing indexes of the string
#   e.g. original: ()() ---> 
#           ( ) ()(), ( ( ) )(), ( () ) (), ( ()( ) ), ( ()() )
#       no spaces: ()()(), (())(), (())() (dupe), (()()), (()()) (dupe)
#       then repeat from other side (move "(" and keep ")" at the end)

#This is O(N * K * M), since we do O(K*M) work each recursive cycle, and due to only calling itself once, there should be N recursive cycles, where N = number of pairs.

print(parens(3))
print(" ")
print(parens(5))


#1 pair: ()
#2 pair: ()(), (())
#3 pair: ()()(), ((())), (()()), ()(()), (())()