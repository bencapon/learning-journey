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

def test_check_winner():
    b = Board()
    # Horizontal win
    for col in range(4):
        b.drop_disc(col, 1)
    assert b.check_winner(1) == True

    # Vertical win
    b = Board()
    for _ in range(4):
        b.drop_disc(0, 1)
    assert b.check_winner(1) == True

    