def palinPermute(str):
    isOdd = False 

    if len(str)%2 == 1: #if number of letter is odd, we can have one solo letter
        isOdd = True
    
    str_list = {}

    #put everything into the hashtable
    for letter in str:
        if letter == " ": #ignore spaces, flip isOdd since length is now one shorter
            isOdd = not isOdd
        else:
            if letter in str_list:
                str_list[letter] += 1
            else:
                str_list[letter] = 1

    #check if all value in the hashtable are even (first odd value excluded if str length is odd)
    for value in str_list:
        if str_list[value]%2 != 0:
            if isOdd:
                isOdd = False #set isOdd to false when first hitting a solo letter
            else:
                return False #extra solo letter = not palindrome
    
    return True

#This is O(N) time. The first for loop is O(N) (runs through the N letters in the string)
#The second loop will always be <= N, so it is absorbed into O(N) which is the final time complexity

print(palinPermute("potato"))
print(palinPermute("giarrigfa"))
print(palinPermute("taco cat"))