# %% 
from connect4_ai.board import Board
H_win=Board()
for col in range(4):
    H_win.drop_disc(col, 1)

H_win.check_winner_last_move(1,-1,3)

print(H_win)
# %%
