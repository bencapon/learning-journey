class Board:
    
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * self.cols for _ in range(self.rows)]

    def drop_disc(self, col: int, player: int) -> bool:
        """Drop a disc into the specified column. Return True if successful."""
        for row in reversed(range(self.rows)):
            if self.grid[row][col] == 0:
                self.grid[row][col] = player
                return True
        return False
    
    def print_board(self):
        """Print the board."""
        for row in self.grid:
            print(" | ".join(str(cell) if cell != 0 else "." for cell in row))
            print("-" * (self.cols * 4 - 3))

    def printgrid(self):
        """Print the grid."""
        for row in range(self.rows):
            print(self.grid[row])

    def check_4(self, row: int, col: int, delta_row: int, delta_col: int, player: int) -> bool:
        """Check if there are 4 in a row in the specified direction."""
        for _ in range(4):
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.grid[row][col] != player:
                return False
            row += delta_row
            col += delta_col
        return True 
    
    
    def check_winner(self, player: int) -> bool:
        """Check if the specified player has won."""
        # Check horizontal, vertical, and diagonal lines for a win
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == player:
                    if self.check_4(row, col, 1, 0, player) or \
                       self.check_4(row, col, 0, 1, player) or \
                       self.check_4(row, col, 1, 1, player) or \
                       self.check_4(row, col, 1, -1, player):
                        return True
        return False




