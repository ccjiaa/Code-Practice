import copy

def power_set(set):
    set_list = [] #create a list to hold the powerset
    set_list = generate_power_set(set, set_list) #initialize the recursion to fill in the powerset list
    set_list.sort() #sort for organization
    set_list.insert(0, [None]) #add the null set as the first value in the powerset

    return set_list
    
    
def generate_power_set(set, power_set):
    if len(set) < 2: #if only one remaining value in the set
        power_set.append(set) #append self to the powerset
        return power_set #return upwards to the previous recursion call
    
    #take off the last value in the set and find the powerset of the new smaller set
    smaller_set = set.copy()
    smaller_set.pop()
    power_set = generate_power_set(smaller_set, power_set)

    #once you have the powerset of the smaller set, copy the smaller set and append the previously popped value to every set in the powerset
    new_power_set = copy.deepcopy(power_set)
    for val in new_power_set:
        val.append(set[len(set) - 1]) #append last number to each value in the old powerset
    
    new_power_set.append([set[len(set) - 1]]) #append the last value in current set as a powerset
    
    power_set = power_set + new_power_set #add the smaller powerset and new larger powerset together

    return power_set #return upwards to the previous recursion


#This is O(N^2) time, since you need to repeatedly do work on N items, N-1 items, N-2, etc, until you reach 1
#The summation of all values from 1 to N is N(N+1)/2, which simplifies to N^2

li = [1, 2, 3]
print(power_set(li))


# [1] -> [1]
# [1, 2] -> [1], [2], [1, 2]
# [1, 2, 3] -> #[1], #[2], #[3], #[1, 2], #[1, 3], #[2, 3], #[1, 2, 3]
# [1, 2, 3, 4] -> [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [2, 3, 4], [1, 2, 4], [1, 2, 3, 4]