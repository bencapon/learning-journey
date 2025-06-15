from connect4_ai.board import Board

def test_drop_disc():
    b = Board()
    assert b.drop_disc(0, 1)
    assert b.grid[-1][0] == 1  # should land in bottom row

def test_drop_disc_full_column():
    b = Board()
    for _ in range(b.rows):
        b.drop_disc(0, 1)  # fill the first column
    assert not b.drop_disc(0, 1)  # should fail to drop in full column  
    assert b.grid[0][0] == 1  # top row should contain of player 1's disc

def test_board_str():
    b= Board()
    assert str(b).count(".") == b.rows * b.cols  # all empty

"""Creating winning boards, where player 1 has won"""
# Horizontal win
H_win=Board()
for col in range(4):
    H_win.drop_disc(col, 1)

# Vertical win
V_win = Board()
for _ in range(4):
    V_win.drop_disc(0, 1)

# Diagonal win (bottom-left to top-right)
D1_win = Board()
for i in range(4):
    for _ in range(i):
        D1_win.drop_disc(i,2)
    D1_win.drop_disc(i, 1)

# Diagonal win (top left to bottom right)
D2_win=Board()
for i in range(4):
    for _ in range(3-i):
        D2_win.drop_disc(i,2)
    D2_win.drop_disc(i,1)

def test_check_winner():
    assert H_win.check_winner(1) == True
    assert V_win.check_winner(1) == True
    assert D1_win.check_winner(1) == True
    assert D2_win.check_winner(1) == True

#here 5 is the bottom row, because there are 6 rows and 7 columns in the default board
def test_check_winner_last_move():
    assert H_win.check_winner_last_move(1,5,3)
    assert V_win.check_winner_last_move(1,2,0)
    assert D1_win.check_winner_last_move(1,2,3)
    assert D2_win.check_winner_last_move(1,5,3)

