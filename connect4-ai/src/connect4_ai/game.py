from connect4_ai.board import Board
from connect4_ai.player import Player
import random

class RandomBot(Player):
    def get_move(self, board: Board) -> int:
        legal_moves = [c for c in range(board.cols) if board.grid[0][c] == 0]
        return random.choice(legal_moves)

def play_game():
    board = Board()
    player1 = RandomBot(1, "Bot 1")
    player2 = RandomBot(2, "Bot 2")
    players = [player1, player2]

    current = 0  # index: 0 or 1
    last_row = 0
    last_col = 0

    
    while True:
        print(board)
        player = players[current]
        col = player.get_move(board)
        print(f"{player.name} chooses column {col}")

        row = board.drop_disc(col, player.number)
        if row is None:
            print("Invalid move, try again.")
            continue

        if board.check_winner_last_move(player.number,row,col):
            print(board)
            print(f"{player.name} wins!")
            break

        if board.is_full():
            print(board)
            print("It's a draw!")
            break

        current = 1 - current  # switch players

if __name__ == "__main__":
    play_game()