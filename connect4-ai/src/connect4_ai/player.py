import random
from connect4_ai.board import Board
class Player:
    def __init__(self, number: int, name: str = "Player"):
        self.number = number  # 1 or 2
        self.name = name

    def get_move(self, board):
        """To be implemented in subclasses (e.g. HumanPlayer, BotPlayer)."""
        raise NotImplementedError
    

class HumanPlayer(Player):
    def get_move(self, board) -> int:
        """Get move from human player."""
        while True: # keep asking for input until a valid move is made
            try: # allow for invalid input, like letters or symbols
                col = int(input(f"Enter column (0-{board.cols - 1}): "))
                if 0 <= col < board.cols: #check if the column is within range
                    return col
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

class RandomBot(Player):
    def get_move(self, board: Board) -> int:
        legal_moves = [c for c in range(board.cols) if board.grid[0][c] == 0] #list of columns that are not full
        return random.choice(legal_moves)