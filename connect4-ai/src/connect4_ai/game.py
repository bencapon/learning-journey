from connect4_ai.board import Board
from connect4_ai.player import Player, RandomBot, HumanPlayer




def play_game():
    board = Board()
    player1 = HumanPlayer(1, "You")
    player2 = RandomBot(2, "Bot")
    players = [player1, player2]

    current = 0  # index: 0 or 1
    last_row = 0
    last_col = 0

    
    while True:
        print(board)
        player = players[current]
        col = player.get_move(board)
        print(f"{player.name} chose column {col}")

        row = board.drop_disc(col, player.number)
        if row is None:
            print("Invalid move, try again.")
            continue

        if board.check_winner_last_move(player.number,row,col):
            print(board)
            print(f"{player.name} won!")
            break

        if board.is_full():
            print(board)
            print("It's a draw!")
            break

        current = 1 - current  # switch players

if __name__ == "__main__":
    play_game()