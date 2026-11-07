import random

class Dice:
    def __init__(self, sides: int = 6) -> None:
        if sides < 2:
            raise ValueError("Need two or more sides")
        self.sides = sides

    def roll(self) -> int:
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        return f"Dice(sides = {self.sides})"

    def __call__(self) -> int:
        return self.roll


d20 = Dice(sides=20)
print("D20 roll:", d20.roll())
