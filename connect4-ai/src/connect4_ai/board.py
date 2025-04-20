class Board:
    ROWS = 6
    COLS = 7

    def __init__(self):
        self.grid = [[0] * self.COLS for _ in range(self.ROWS)]

    def drop_disc(self, col: int, player: int) -> bool:
        """Drop a disc into the specified column. Return True if successful."""
        for row in reversed(range(self.ROWS)):
            if self.grid[row][col] == 0:
                self.grid[row][col] = player
                return True
        return False