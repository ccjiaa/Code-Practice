class Piece:
    def __init__



class Othello:
    def __init__(self, name_1, name_2):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, "white", "black", 0, 0, 0],
                      [0, 0, 0, "black", "white", 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],]

        self.white = name_1 #changes 0 to "white"
        self.black = name_2 #changes 0 to "black"
        self.score_white = 0
        self.score_black = 0

    #method to place a piece
    def place_piece(self, player, row, col):
        if player is name_1:
            color = "white"
        else:
            color = "black"

        if self.board[row][col] is 0:
            is_invalid_move = False
            #need to check for flipping
            if row is 0: #top row
                if col is 0: #top left corner
                    if not self.is_surround_down(row, col, color) and not self.is_surround_right(row, col, color) and not self.is_surround_down_right(row, col, color): #if no pieces were flipped
                        is_invalid_move = True
                elif col is 7: #top right corner
                    if not self.is_surround_down(row, col, color) and not self.is_surround_left(row, col, color) and not self.is_surround_down_left(row, col, color): #if no pieces were flipped
                        is_invalid_move = True
                else: #anything else in top row
                    if not self.is_surround_down(row, col, color) and not self.is_surround_left(row, col, color) and not self.is_surround_down_left(row, col, color) 
                    and not self.is_surround_right(row, col, color) and not self.is_surround_down_right(row, col, color): #if no pieces were flipped
                        is_invalid_move = True
            elif row is 7: #bottom row
                if col is 0: #bottom left corner
                    if not self.is_surround_up(row, col, color) and not self.is_surround_right(row, col, color) and not self.is_surround_up_right(row, col, color): #if no pieces were flipped
                        is_invalid_move = True
                elif col is 7: #bottom right corner
                    if not self.is_surround_up(row, col, color) and not self.is_surround_left(row, col, color) and not self.is_surround_up_left(row, col, color): #if no pieces were flipped
                        is_invalid_move = True
                else: #anything else in bottom row
                    if not self.is_surround_up(row, col, color) and not self.is_surround_left(row, col, color) and not self.is_surround_up_left(row, col, color) 
                    and not self.is_surround_right(row, col, color) and not self.is_surround_up_right(row, col, color): #if no pieces were flipped
                        is_invalid_move = True
            else: #if any other row
                if col is 0: #leftmost column
                    if not self.is_surround_down(row, col, color) and not self.is_surround_right(row, col, color) and not self.is_surround_down_right(row, col, color)
                    not self.is_surround_up(row, col, color) and not self.is_surround_up_right(row, col, color): #if no pieces were flipped
                        is_invalid_move = True
                elif col is 7: #rightmost column
                    if not self.is_surround_down(row, col, color) and not self.is_surround_left(row, col, color) and not self.is_surround_down_left(row, col, color)
                    not self.is_surround_up(row, col, color) and not self.is_surround_up_left(row, col, color): #if no pieces were flipped
                        is_invalid_move = True
                else: #any space inside the outer edge spaces of the board
                    if not self.is_surround_down(row, col, color) and not self.is_surround_left(row, col, color) and not self.is_surround_down_left(row, col, color) 
                    and not self.is_surround_right(row, col, color) and not self.is_surround_down_right(row, col, color) not self.is_surround_up(row, col, color) 
                    and not self.is_surround_up_left(row, col, color) and not self.is_surround_up_right(row, col, color): #all 8 directions
                        is_invalid_move = True
            
            if is_invalid_move:
                return "Invalid move."
            self.board[row][col] = color #place piece at end
                
            for row in board:
                print(row)
            return 1 #indications successful move
        else:
            return "Invalid move, space occupied."

    #reverses input color
    def opposite_color(self, player_color):
        if player_color is "white":
            return "black"
        else:
            return "white"

#Check for flanking ------------------------------------------------------------------------------------------------------------------------------------
    #check if flanking pieces above, returns true if pieces were flipped, false if no pieces were flipped
    def is_surround_up(self, row, col, color):
        is_flip = False #variable to check if a piece has been flanked and flipped
        opposite_color = self.opposite_color(color)
        is_opposite_between = False

        temp_row = row - 1 #start at previous row
        while temp_row >= 0: #until you reach first row
            if self.board[temp_row][col] is opposite_color:
                is_opposite_between = True
            if self.board[temp_row][col] is 0: #if you encounter 0, break, keep is_flip false
                break
            elif self.board[temp_row][col] is color: #if you encounter same number, break, set is_flip to true
                if is_opposite_between:
                    is_flip = True
                    break
                else:
                    continue
            temp_row -= 1

        if is_flip:
            original_row = row - 1 #make a new temp_row
            while original_row > temp_row:
                self.board[original_row][col] = color #flip flanked pieces
                original_row -= 1
            return True
        return False
        
    #check if flanking pieces below, could have been coupled with is_surround_up using if statements, but difficult to reduce size due to inequalities
    def is_surround_down(self, row, col, color):
        is_flip = False
        opposite_color = self.opposite_color(color)
        is_opposite_between = False
        
        temp_row = row + 1 #start at previous row
        while temp_row <= 7:
            if self.board[temp_row][col] is opposite_color:
                is_opposite_between = True
            if self.board[temp_row][col] is 0: #if you encounter 0, break, keep is_flip false
                break
            elif self.board[temp_row][col] is color: #if you encounter same number, break, set is_fli pto true
                if is_opposite_between:
                    is_flip = True
                    break
                else:
                    continue
            temp_row += 1

        if is_flip:
            original_row = row + 1 #make a new temp_row
            while original_row < temp_row:
                self.board[original_row][col] = color
                original_row += 1
            return True
        return False

    #check if flanking pieces to the left
    def is_surround_left(self, row, col, color):
        is_flip = False
        opposite_color = self.opposite_color(color)
        is_opposite_between = False
        
        temp_col = col - 1 #start at previous row
        while temp_col >= 0:
            if self.board[row][temp_col] is opposite_color:
                is_opposite_between = True
            if self.board[row][temp_col] is 0: #if you encounter 0, break, keep is_flip false
                break
            elif self.board[row][temp_col] is color: #if you encounter same number, break, set is_fli pto true
                if is_opposite_between:
                    is_flip = True
                    break
                else:
                    continue
            temp_col -= 1

        if is_flip:
            original_col = col - 1 #make a new temp_row
            while original_col > temp_col:
                self.board[row][original_col] = color
                original_col -= 1
            return True
        return False

    #check is flanking pieces to the right
    def is_surround_right(self, row, col, color):
        is_flip = False
        opposite_color = self.opposite_color(color)
        is_opposite_between = False
        
        temp_col = col + 1 #start at previous row
        while temp_col <= 7:
            if self.board[row][temp_col] is opposite_color:
                is_opposite_between = True
            if self.board[row][temp_col] is 0: #if you encounter 0, break, keep is_flip false
                break
            elif self.board[row][temp_col] is color: #if you encounter same number, break, set is_flip to true
                if is_opposite_between:
                    is_flip = True
                    break
                else:
                    continue
            temp_col += 1

        if is_flip:
            original_col = col + 1 #make a new temp_row
            while original_col < temp_col:
                self.board[row][original_col] = color
                original_col += 1
            return True
        return False

    #check if flanking pieces up left
    def is_surround_up_left(self, row, col, color):
        is_flip = False
        opposite_color = self.opposite_color(color)
        is_opposite_between = False
        
        temp_row = row - 1 #start at previous row
        temp_col = col - 1 #start at previous col
        while temp_col >= 0 and temp_row >= 0:
            if self.board[temp_row][temp_col] is opposite_color:
                is_opposite_between = True
            if self.board[temp_row][temp_col] is 0: #if you encounter 0, break, keep is_flip false
                break
            elif self.board[temp_row][temp_col] is color: #if you encounter same number, break, set is_fli pto true
                if is_opposite_between:
                    is_flip = True
                    break
                else:
                    continue
            temp_row -= 1
            temp_col -= 1

        if is_flip:
            original_row = row - 1 #make a new temp_row (only need row since diagonal means you traverse the same number of rows and cols)
            original_col = col - 1
            while original_row > temp_row:
                self.board[original_row][original_col] = color
                original_row -= 1
                original_col -= 1
            return True
        return False

    #check if flanking pieces up right
    def is_surround_up_right(self, row, col, color):
        is_flip = False
        opposite_color = self.opposite_color(color)
        is_opposite_between = False
        
        temp_row = row - 1 #start at previous row
        temp_col = col + 1 #start at previous col
        while temp_col <= 7 and temp_row >= 0:
            if self.board[temp_row][temp_col] is opposite_color:
                is_opposite_between = True
            if self.board[temp_row][temp_col] is 0: #if you encounter 0, break, keep is_flip false
                break
            elif self.board[temp_row][temp_col] is color: #if you encounter same number, break, set is_fli pto true
                if is_opposite_between:
                    is_flip = True
                    break
                else:
                    continue
            temp_row -= 1
            temp_col += 1

        if is_flip:
            original_row = row - 1 #make a new temp_row (only need row since diagonal means you traverse the same number of rows and cols)
            original_col = col + 1
            while original_row > temp_row:
                self.board[original_row][original_col] = color
                original_row -= 1
                original_col += 1
            return True
        return False

    #check if flanking pieces bottom left
    def is_surround_down_left(self, row, col, color):
        is_flip = False
        opposite_color = self.opposite_color(color)
        is_opposite_between = False
        
        temp_row = row + 1 #start at previous row
        temp_col = col - 1 #start at previous col
        while temp_col >= 0 and temp_row <= 7:
            if self.board[temp_row][temp_col] is opposite_color:
                is_opposite_between = True
            if self.board[temp_row][temp_col] is 0: #if you encounter 0, break, keep is_flip false
                break
            elif self.board[temp_row][temp_col] is color: #if you encounter same number, break, set is_fli pto true
                if is_opposite_between:
                    is_flip = True
                    break
                else:
                    continue
            temp_row += 1
            temp_col -= 1

        if is_flip:
            original_row = row + 1 #make a new temp_row (only need row since diagonal means you traverse the same number of rows and cols)
            original_col = col - 1
            while original_row < temp_row:
                self.board[original_row][original_col] = color
                original_row += 1
                original_col -= 1
            return True
        return False

    #check if flanking pieces bottom right
    def is_surround_down_right(self, row, col, color):
        is_flip = False
        opposite_color = self.opposite_color(color)
        is_opposite_between = False
        
        temp_row = row + 1 #start at previous row
        temp_col = col + 1 #start at previous col
        while temp_col <= 7 and temp_row <= 7:
            if self.board[temp_row][temp_col] is opposite_color:
                is_opposite_between = True
            if self.board[temp_row][temp_col] is 0: #if you encounter 0, break, keep is_flip false
                break
            elif self.board[temp_row][temp_col] is color: #if you encounter same number, break, set is_fli pto true
                if is_opposite_between:
                    is_flip = True
                    break
                else:
                    continue
            temp_row += 1
            temp_col += 1

        if is_flip:
            original_row = row + 1 #make a new temp_row (only need row since diagonal means you traverse the same number of rows and cols)
            original_col = col + 1
            while original_row < temp_row:
                self.board[original_row][original_col] = color
                original_row += 1
                original_col += 1
            return True
        return False

#Check for flanking end ------------------------------------------------------------------------------------------------------------------------------------

    #checks if board is full
    def is_board_full(self):
        #check for zeroes, if zero present, not full, return false, else return true
        for row in self.board:
            if 0 in row:
                return False

        return True

    #reset board
    def reset(self):
        self.__init__(self.white, self.black) #call init again

    #Tallies points and announces winner/draw
    def count_score(self):
        #traverse through matrix and count black and white pieces
        for row in self.board:
            for col in row:
                if col is "white":
                    self.score_white += 1
                elif col is "black":
                    self.score_black += 1
                else:
                    continue
        
        #print raw scores
        print(self.white + "'s score: " + str(self.score_white))
        print(self.black + "'s score: " + str(self.score_black))

        #print winner
        if self.score_white > self.score_black:
            print(self.white + " wins!")
        elif self.score_black > self.score_white:
            print(self.black + " wins!")
        else:
            print("Tie!")