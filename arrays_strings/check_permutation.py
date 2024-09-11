def checkPermutation(str1, str2):
    if len(str1) != len(str2): #if not same length can't be permutations
        return False
    
    letterDict = {} #create hashtable to hold unique letters

    for letter in str1:
        if letter in letterDict:
            letterDict[letter] += 1 #add one to the amount if letter already in the hashtable
        else:
            letterDict[letter] = 1 #else add the new letter to the hashtable

    for letter in str2:
        if letter not in letterDict:
            return False #not in means that a letter in str2 is not in str1 thus not permutations
        else:
            letterDict[letter] -= 1 #otherwise subtract amount by 1
    
    for value in letterDict:
        if letterDict[value] != 0: #accounts for different numbers of duplicates
            return False
        
    return True

#To get to the for loops, str1 and str2 must be same length, so we can assume their lengths are both "N"
#Thus, the two upper for loops have O(2N) time which is just O(N) time
#The third for loop goes as long as letterDict is, and letterDict's length is always less than or
# equal to str1's length. Thus, it gets absorbed by the O(N), making the total time of this program O(N)

print(checkPermutation("potato", "optaot"))
print(checkPermutation("potato", "potatee"))
print(checkPermutation("potato", "potata"))
