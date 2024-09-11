def URLify(str):
    if " " not in str: #check if there are spaces in the first place
        return str
    
    str_list = []

    #place everything in the list, replacing spaces
    for letter in str:
        if letter == " ":
            str_list.append("%20")
        else:
            str_list.append(letter)

    return "".join(str_list) #concatenate everything in the list.
    

#The search of spaces in str takes O(N) time, where N is the length of the string
#Likewise, putting everything into the list also takes O(N) time
#Finally the join efficiently concatenates everything in the string

print(URLify("Amber is best girl"))