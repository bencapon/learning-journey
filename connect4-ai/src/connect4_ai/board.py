class Board:
    EMPTY=0

    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * self.cols for _ in range(self.rows)]

    def drop_disc(self, col: int, player: int) -> bool:
        """Drop a disc into the specified column. Return True if successful."""
        for row in reversed(range(self.rows)):
            if self.grid[row][col] == 0:
                self.grid[row][col] = player
                return row #return the row the disc landed on
        return None # column is full 
    
    def __str__(self):
        symbols = {0: ".", 1: "X", 2: "O"}
        rows = [" ".join(symbols[c] for c in row) for row in self.grid]
        return "\n".join(rows)

    def check_4(self, row: int, col: int, delta_row: int, delta_col: int, player: int) -> bool:
        """Check if there are 4 in a row in the specified direction."""
        for _ in range(4):
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.grid[row][col] != player:
                return False
            row += delta_row
            col += delta_col
        return True 
    
    
    def check_winner(self, player: int) -> bool:
        """Check if the specified player has won, scanning the whole board.
        Check horizontal, vertical, and diagonal lines for a win"""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == player:
                    if self.check_4(row, col, 1, 0, player) or \
                       self.check_4(row, col, 0, 1, player) or \
                       self.check_4(row, col, 1, 1, player) or \
                       self.check_4(row, col, 1, -1, player):
                        return True
        return False
    
    def check_winner_last_move(self, player: int, row: int, col: int) -> bool:
        """Check if the specified player has won with the last move."""
        #Check vertical (only down)
        if self.check_4(row, col, 1, 0, player):
            return True
        #Horizontal 
        if self.check_4(row, col, 0, 1, player) or self.check_4(row, col, 0, -1, player):
            return True
        #Check diag, top left to bottom right
        if self.check_4(row, col, 1, 1, player) or self.check_4(row, col, -1, -1, player):
            return True
        #diag, bottom left to top right
        if self.check_4(row, col, 1, -1, player) or self.check_4(row, col, -1, 1, player):
            return True
        
        return False
    

    def is_full(self) -> bool:
        """Return True if the board is full (i.e., no empty cells in the top row)."""
        return all(cell != self.EMPTY for cell in self.grid[0])



