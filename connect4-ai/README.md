Lose at connect 4 against an AI

Notes:

Why is the file structure learning-journey\connect4-ai\src\connect4_ai ? What is the point of the connect4_ai folder inside src?
It defines a proper Python package called "connect4_ai". This allows me to import using 
>from connect4_ai.board import Board
importing from src.board isn't very clean or portable

Why define a function play_game and call it if __name__ == "__main__", instead of just having the play_gmae script as top level code?
1. So that play_game is only run if the game file is being run directly (not imported by another file).
2. Keeps the game reusable, testable, and organised. Considered best practice in every Python script. 