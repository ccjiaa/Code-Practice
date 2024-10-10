def paint_fill(row, col, screen, new_color):
    fill(screen[row][col], row, col, screen, new_color) #initialize recursion
    return


def fill(original_color, row, col, screen, new_color):
    if original_color != screen[row][col]: #if the color of the current pixel is not the same as the color of the original point
        return #do nothing
    
    screen[row][col] = new_color #change color to new color

    #do above for all 4 cardinally adjacent pixels
    if row - 1 > -1:
        fill(original_color, row - 1, col, screen, new_color)
    if row + 1 < len(screen):
        fill(original_color, row + 1, col, screen, new_color)
    if col - 1 > 0:
        fill(original_color, row, col - 1, screen, new_color)
    if col + 1 < len(screen[row]):
        fill(original_color, row, col + 1, screen, new_color)

    return

#This is O(4^N) time as each recursive call does constant work, but there are four calls per recursive call, so 4 branches


canvas = [[1, 1, 1, 2, 2, 3, 1, 1],
          [1, 1, 3, 2, 2, 3, 1, 1],
          [1, 1, 3, 3, 3, 3, 2, 2], 
          [1, 1, 2, 2, 2, 3, 2, 2],
          [1, 1, 3, 2, 2, 3, 1, 1]]
print("before")
for row in canvas:
    print(row)

paint_fill(2, 2, canvas, 0)

print("\nafter")
for row in canvas:
    print(row)