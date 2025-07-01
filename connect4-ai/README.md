Lose at connect 4 against an AI

Notes:

Why is there file structure learning-journey\connect4-ai\src\connect4_ai ? What is the point of the connect4_ai folder inside src?

1. It defines a proper Python package called "connect4_ai"
This allows me to import using 
>from connect4_ai.board import Board
importing from src.board isn't very clean or portable

