def robot_grid(grid):
    move_list = [] #create a list to hold the list of moves to get to the bottom right

    #if only one row
    if len(grid) == 1:
        if False in grid[0]:
            return "No path"
        else:
            for x in range(len(grid[0])):
                move_list.append("right")
        return move_list
    
    #if only one column
    if len(grid[0]) == 1:
        for y in range(len(grid)):
            if not grid[y][0]: #if encounter a forbidden square
                return "No path"
            else: 
                move_list.append("right")
        return move_list


    #find dimensions of the matrix
    max_row_len = len(grid)
    max_col_len = len(grid[max_row_len - 1])

    #create a matrix using those dimensions to hold number of paths through a square
    map_row = [0] * max_col_len
    path_map = []

    for row in range(max_row_len):#create a new empty array to store path data
        path_map.append(map_row.copy()) 

    for i in range(max_row_len):
        if grid[i][0] == False: #if there is a forbidden square in the first column
            break
        else:
            path_map[i][0] = 1 #else, set number of paths equal to 1

    for k in range(max_col_len):
        if grid[0][k] == False: #if there is a forbidden square in the first row
            break
        else:
            path_map[0][k] = 1 #else, set number of paths equal to 1

    increment_paths(grid, path_map, max_row_len - 1, max_col_len - 1) #increment paths that have a path to the goal

    #travel through the grid according to the path availabilities from path_map
    travel_row = 0
    travel_col = 0
    while travel_row < max_row_len - 1 or travel_col < max_col_len - 1:
        if path_map[travel_row + 1][travel_col] == 0 and path_map[travel_row][travel_col + 1] == 0: #if there are no paths forward
            return "No path"
        if travel_row < max_row_len - 1: #if not at last row
            if path_map[travel_row + 1][travel_col] > 0: #travel down 1 row
                move_list.append("down")
                travel_row += 1
        if travel_col < max_col_len - 1: #if not at last col
            if path_map[travel_row][travel_col + 1]: #travel right one col
                move_list.append("right")
                travel_col += 1

    return move_list


def increment_paths(grid, map, row, col):
    if row < 0 or col < 0 or not grid[row][col]:
        return
    
    if not grid[row][col]: #if that grid square is forbidden
        return #exit
    
    if map[row][col] > 0: #if path is already confirmed to work
        return #break and exit
    
    map[row][col] = 1

    increment_paths(grid, map, row - 1, col)
    increment_paths(grid, map, row, col - 1)



mat = [[True, True, False, True], 
       [False, False, True, True], 
       [True, True, True, True]]

mat2 = [[True],
        [False],
        [True]]

mat3 = [[True, True, True, True], 
       [False, False, True, True], 
       [True, True, True, True]]

print(robot_grid(mat))
print(robot_grid(mat2))
print(robot_grid(mat3))

[[1, 1, 1, 1], 
 [0, 0, 1, 1], 
 [1, 1, 1, 1]]