from dice import Dice


class Weapon:
    """Represents a weapon in the RPG"""
    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Weapon
        Args:
        name (str): The name of the weapon.
        damage_dice (Dice): calls the Dice class to roll the weapons damage
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        return self.damage_dice.roll()

    def __str__(self) -> str:
        return f'{self.name} with damage dice d{self.damage_dice.sides}'

d8 = Dice(sides=8)
sword = Weapon(name='sword', damage_dice=d8)
print('sword damage (d8):', sword.roll_damage())
