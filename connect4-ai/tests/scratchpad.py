# %% 
from connect4_ai.board import Board
b = Board()
for col in range(b.cols):
    for _ in range(b.rows):
        b.drop_disc(col, 1 if col % 2 == 0 else 2)  # alternate players

print(b)
# %%
