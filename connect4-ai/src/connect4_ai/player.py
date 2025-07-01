import random
from connect4_ai.board import Board
class Player:
    def __init__(self, number: int, name: str = "Player"):
        self.number = number  # 1 or 2
        self.name = name

    def get_move(self, board):
        """To be implemented in subclasses (e.g. HumanPlayer, BotPlayer)."""
        raise NotImplementedError
    

def HumanPlayer(Player):
    def get_move(self, board):
        """Get move from human player."""
        while True: # keep asking for input until a valid move is made
            try: # allow for invalid input, like letters or symbols
                col = int(input(f"{self.name} (Player {self.number}), enter column (0-{board.cols - 1}): "))
                if 0 <= col < board.cols and board.drop_disc(col, self.number): #check if the column is within range and is not full
                    return col
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

class RandomBot(Player):
    def get_move(self, board: Board) -> int:
        legal_moves = [c for c in range(board.cols) if board.grid[0][c] == 0]
        return random.choice(legal_moves)