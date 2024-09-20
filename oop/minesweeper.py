from random import random
class Tile:
    def __init__(self):
        self.bomb = False
        self.num = 0
        self.hidden = True
        self.marked = False

    def increment_num(self):
        self.num += 1

    def toggle_mark(self):
        self.marked = not self.marked
    
    def toggle_hidden(self):
        self.hidden = not self.hidden

    def toggle_bomb(self):
        self.bomb = not self.bomb


class Minesweeper:
    def __init__(self, size, num_bombs):
        self.size = size

        #create the minefield rows
        minefield_row = []
        for i in range(size):
            minefield_row.append(Tile())

        #create the minefield proper
        self.minefield = []
        for i in range(size):
            temp_row = minefield_row.copy()
            self.minefield.append(temp_row)

        #plant the bombs in random coordinates
        bomb_count = 0
        while bomb_count < num_bombs:
            row = random.randrange(0, size, 1)
            col = random.randrange(0, size, 1)

            if not self.minefield[row][col].bomb:
                self.minefield[row][col].toggle_bomb() #set tile to bomb tile

                #increment num of all surrounding tiles
                if row > 0: #if not in topmost row
                    self.minefield[row - 1][col].num += 1 #increase num of tile directly above
                    if col > 0: #if not in leftmost column either
                        self.minefield[row - 1][col - 1].num += 1 #increase num of tile to the upper left
                    if col < self.size: #if not in rightmost column either
                        self.minefield[row - 1][col + 1].num += 1 #increase num of tile to the upper right
                if row < self.size: #if not in bottommost row
                    self.minefield[row + 1][col].num += 1 #increase num of tile directly below
                    if col > 0: #if not in leftmost column either
                        self.minefield[row + 1][col - 1].num += 1 #increase num of tile to the lower left
                    if col < self.size: #if not in rightmost column either
                        self.minefield[row + 1][col + 1].num += 1 #increase num of tile to the lower right
                if col > 0: #if not in leftmost column
                    self.minefield[row][col - 1].num += 1 #increase num of tile to the left
                if col < self.size: #if not in rightmost column
                    self.minefield[row][col + 1].num += 1 #increase num of tile to the right
                
                bomb_count += 1 #increment number of bombs planted

    #prints all tiles
    def print(self):
        for row in minefield:
            for col in minefield:
                if col.marked:
                    print("M", end = " ")
                elif col.hidden:
                    print("H", end = " ")
                else:
                    print(col.num, end = " ")
            print("\n")


    #reveals a chosen tile
    def reveal_tile(self, row, col):
        if row > self.size or col > self.size or row < 0 or col < 0:
            return "Invalid coordinate, out of scope."
        
        if not self.minefield[row][col].hidden: #if tile already revealed
            return "Tile already revealed."
        elif self.minefield[row][col].marked:
            return "Invalid coordinate, marked tile. Please un-mark first."
        elif self.minefield[row][col].bomb:
            print("Game over.")
        elif self.minefield[row][col].num == 0: #if 0, reveal surrounding 8 tiles (guaranteed to not be mine)
            self.reveal_tile(row - 1, col - 1) #top left
            self.reveal_tile(row - 1, col)     #top
            self.reveal_tile(row - 1, col + 1) #top right
            self.reveal_tile(row, col + 1)     #right
            self.reveal_tile(row + 1, col + 1) #bottom right
            self.reveal_tile(row + 1, col)     #bottom
            self.reveal_tile(row + 1, col - 1) #bottom left
            self.reveal_tile(row, col - 1)     #left

        self.print()