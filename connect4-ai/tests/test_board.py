from connect4_ai.board import Board

def test_drop_disc():
    b = Board()
    assert b.drop_disc(0, 1)
    assert b.grid[-1][0] == 1  # should land in bottom row