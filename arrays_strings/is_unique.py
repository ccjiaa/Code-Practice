def isUnique(str):
    strings  = {}
    for letter in str:
        if (letter in strings):
            return False
        strings[letter] = letter
    return True

print (isUnique("absd"))
print (isUnique("potato"))

#O(s^2) time, since worst case it will need to iterate through the entire string and the entire dictionnary
#really really bad
#changed second loop to "in" operator, apparently O(1) time for dictionnaries? So now this would be O(N) time

