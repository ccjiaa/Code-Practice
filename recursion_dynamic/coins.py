def coins(sum):
    if sum < 0: #if overshoot, not a solution, return 0
        return 0
    if sum == 0: #if equal to zero, solution, return 1
        return 1
    
    ways = 0

    #check each possibility
    ways += coins(sum - 1)
    ways += coins(sum - 5)
    ways += coins(sum - 10)
    ways += coins(sum - 25)

    return ways


#Counts permutations, order matters
#This is O(4^N) time since constant work with 4 branches. However, it's possible to reduce this time using memorization (will update eventually)

print(coins(6))