class Player:
    def __init__(self, number: int, name: str = "Player"):
        self.number = number  # 1 or 2
        self.name = name

    def get_move(self, board):
        """To be implemented in subclasses (e.g. HumanPlayer, BotPlayer)."""
        raise NotImplementedError