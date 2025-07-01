# %% 
from connect4_ai.board import Board
import connect4_ai.game as game

BASE_DIRS = [
    (dr, dc)
    for dr in (0, 1)
    for dc in (-1, 0, 1)
    if (dr, dc) != (0, 0) and not (dr == 0 and dc == -1)
]

for dr, dc in BASE_DIRS:
    print(f"Direction: {dr}, {dc}")

# %%
