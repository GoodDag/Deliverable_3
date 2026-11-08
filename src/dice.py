import random


class Dice:
    """The dice that will be used in the game"""
    def __init__(self, sides: int = 6) -> None:
        """
        Initialize the dice
        Args:
        sides (int): sets the default amount of sides on the dice
        """
        if sides < 2:
            raise ValueError("Need two or more sides")
        self.sides = sides

    def roll(self) -> int:
        """Gives the dice a random amount of sides"""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Representation of the dice"""
        return f"Dice(sides = {self.sides})"

    def __call__(self) -> int:
        """Allows the dice to be called"""
        return self.roll()
