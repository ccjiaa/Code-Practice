#need puzzle piece, with 4 sides, each side has a code that will match the code of a side on another piece
#need puzzle itself to store all the pieces

class Puzzle_Piece:
    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

class Puzzle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.total_pieces = height * width
        self.completion percentage = 0
        self.board = []
        for row in range(height):
            for col in range(width):
                temp_piece = Puzzle_Piece(0, 0, 0, 0)
                board.append(temp_piece)

        board[0][0].left = 1
        board[0][0].top = 2
        board[0][0].left = 3
        board[0][0].bottom = 4
        for piece in board:
            #continue here
            
    def fits_with(self, edge_1, edge_2):
        if edge_1 = edge_2:
            return True
        return False

    
#Algorithm: first find the corner pieces, then find the edge pieces
#now you have the outer circumference of the NxN puzzle, which means you essentially
#have an (N-1)x(N-1) puzzle. Repeat the algorithm for the smaller puzzle after taking out 
#the pieces in the outer circumference from the list of valid pieces. Continue until you reach the center