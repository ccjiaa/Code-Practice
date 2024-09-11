def one_away(str1, str2):
    if len(str1) - len(str2) > 1 or len(str1) - len(str2) < -1: #if length differs by 2 or more, false
        return False
    
    one_change_allowed = True

    #equal length case
    #one different letter allowed, everything else must be the same
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if one_change_allowed:
                    one_change_allowed = False #one chance to have different letter used up
                else:
                    return False
        return True
    else:
        long_str = ""
        short_str = ""
        if len(str1) > len(str2):
            long_str = str1
            short_str = str2
        else:
            long_str = str2
            short_str = str1
        
        long_idx = 0
        short_idx = 0
        while short_idx < len(short_str) - 1: #iterates through each index of the shorter string
            if short_str[short_idx] != long_str[long_idx]:
                if one_change_allowed:
                    one_change_allowed = False #one change to have different letter used up
                    short_idx -= 1 #difference will always be an inserted character, keep short_idx in place this iteration to check if the rest of longer_str is the same
                else:
                    return False
                
            long_idx += 1 #increment index
            short_idx += 1

        return True
    
    return False #if something goes wrong, assume false

#This is O(N) time.
#First for loop at most goes through each index of str1, whose length we take as N, so O(N) time
#The second case is a while loop that at most goes through every index of str1 + 1 (since when difference in length is >= 2, we always return false)
# So it is O(N + 1) time or simplified to O(N) time
#Either case is O(N) time, which is also the least possible time since we will always need to touch each letter to check for differences. 


print(one_away("bake", "bale"))
print(one_away("bakes", "bake"))
print(one_away("baske", "bake"))
print(one_away("baste", "bake"))
print(one_away("pale", "bake"))
print(one_away("pale", "sbake"))