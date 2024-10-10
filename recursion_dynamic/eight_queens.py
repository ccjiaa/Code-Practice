import copy

def eight_queens_initial():
    board = [[1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]]
    
    board_list = []

    for row in range(8):
        for col in range(8):
            temp_board = copy.deepcopy(board)
            temp_board[row][col] = "Q"
            queen_sight(temp_board, row, col)
            eight_queens(temp_board, 1, board_list)

    return board_list
    
def eight_queens(cur_board, num_queens, board_list):
    if num_queens > 8:
        board_list.append(cur_board)
        return
    
    for row in range(8):
        for col in range(8):
            cur_board[row][col] = "Q"
            queen_sight(cur_board, row, col)
            eight_queens(cur_board, num_queens + 1, board_list)
    
    return


def queen_sight(board, row, col):
    for i in range(8):
        board[row][i] = " " #set same row to empty space
    for j in range(8):
        board[j][col] = " " #set same column to empty space

    temp_row = row - 1
    temp_col = col - 1
    while temp_row > -1 and temp_col > -1:
        board[temp_row][temp_col] = " " #set up left diagonal to empty space
        temp_row -= 1
        temp_col -= 1

    temp_row = row + 1
    temp_col = col + 1
    while temp_row < 8 and temp_col < 8:
        board[temp_row][temp_col] = " " #set down right diagonal to empty space
        temp_row += 1
        temp_col += 1

    temp_row = row + 1
    temp_col = col - 1
    while temp_row < 8 and temp_col > -1:
        board[temp_row][temp_col] = " " #set down left diagonal to empty space
        temp_row += 1
        temp_col -= 1

    temp_row = row - 1
    temp_col = col + 1
    while temp_row > -1 and temp_col < 8:
        board[temp_row][temp_col] = " " #set up right diagonal to empty space
        temp_row -= 1
        temp_col += 1

    return


queens = eight_queens_initial()

for board in queens:
    for row in board:
        print(row)
    print(" ")