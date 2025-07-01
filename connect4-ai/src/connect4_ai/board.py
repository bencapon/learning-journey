class Board:
    EMPTY=0
    BASE_DIRS = [
        (dr, dc)
        for dr in (0, 1)
        for dc in (-1, 0, 1)
        if (dr, dc) != (0, 0) and not (dr == 0 and dc == -1)
    ]
    # → [(0, 1), (1, -1), (1, 0), (1, 1)]
    """
    Base directions for checking 4 in a line:
    - (0, 1): horizontal right 
    - (1, -1): diagonal down-left
    - (1, 0): vertical down
    - (1, 1): diagonal down-right
    Not really necessary to generate base directions programmatically, but it's a good exercise."""

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

    
    def count_discs_in_a_line(self, row: int, col: int, delta_row: int, delta_col: int, player: int) -> int:
        """Count the number of consecutive discs in a line for the specified player."""
        count = 0
        row, col = row + delta_row, col + delta_col #start checking from the next cell in the specified direction
        while 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == player:
            count += 1
            row += delta_row
            col += delta_col
        return count

    def check_winner(self, player: int) -> bool:
            """
            Check if the specified player has won, scanning the whole board.
            Check horizontal, vertical, and diagonal lines for a win.
            This method is not used in the game, but it's useful for testing purposes."""
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.grid[row][col] == player:
                        for dr, dc in self.BASE_DIRS:
                            if self.count_discs_in_a_line(row, col, dr, dc, player) >= 3: # 3 + 1 for the disc itself
                                return True
            return False
    
    def check_winner_last_move(self, player: int, row: int, col: int) -> bool:
        """Check if the specified player has won with the last move."""
        for dr, dc in self.BASE_DIRS: #check 4 base directions
            count = 1 # start with 1 for the last disc placed
            count += self.count_discs_in_a_line(row, col, dr, dc, player) #forward
            count += self.count_discs_in_a_line(row, col, -dr, -dc, player) #backward
            if count >= 4:
                return True
        
        return False
    
    def is_full(self) -> bool:
        """Return True if the board is full (i.e., no empty cells in the top row)."""
        return all(cell != self.EMPTY for cell in self.grid[0])



