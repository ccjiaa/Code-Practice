def string_compression(str):
    if len(str) < 3: #each repeated character will be 2 characters at least, so strings < 3 characters will never be shorter
        return str
    
    letter_dict = {}

    #put everything in hashtable
    for letter in str:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1

    letter_list = []

    str_idx = 0

    #place everything in the hashtable into a list for efficient concatenation
    for key in letter_dict:
        letter_list.append(str[str_idx])
        letter_list.append("%s" % letter_dict[key])
        str_idx += letter_dict[key]

    #concatenate
    compressed_str = "".join(letter_list)
    
    #check if concatenated string is shorter than the original, return if so
    if len(compressed_str) < len(str):
        return compressed_str
    
    #default return original string
    return str

#Since we need to check every character in the string, the minimal time is O(N) where N = length of string
#Putting everything into a hashtable takes O(N) time
#The hashtable at worst has a bit more than double as many values as the original string (character + number)
#Thus putting everything into the list is at worst about O(2N) time, simplifies to O(N) time
#Using join for concatenation also takes O(N) time
#Thus total time is O(N + 2N + N) = O(4N) which simplifies to O(N) time

print(string_compression("aaaabbcdddd"))
print(string_compression("abcds"))
print(string_compression("AAb"))
print(string_compression("AAaaaab"))