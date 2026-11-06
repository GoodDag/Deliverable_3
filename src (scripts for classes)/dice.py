import random

class dice:
    def __init__(self, sides: int = 6):
        if sides < 2:
            raise ValueError("Need two or more sides")
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

    def __repr__(self):
        return f"Dice(sides = {self.sides})"

    def __call__(self):
        return self.roll


d20 = dice(sides=2)
print("D20 roll:", d20.roll())