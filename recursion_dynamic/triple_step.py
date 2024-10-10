def triple_step(num_steps):
    #base cases to ensure that we don't go into the negatives with the multi-steps
    if num_steps < 2:
        return 1
    if num_steps < 3:
        return 2
    if num_steps < 4:
        return 4
    
    num_ways = 0

    #add a path for each step taken (since each combination of steps are unique)
    num_ways = num_ways + triple_step(num_steps - 1)
    num_ways = num_ways + triple_step(num_steps - 2)
    num_ways = num_ways + triple_step(num_steps - 3)

    return num_ways


print(triple_step(4))
#Possible combinations are: 1111, 112, 13, 121, 211, 31, 22 (total 7 paths)