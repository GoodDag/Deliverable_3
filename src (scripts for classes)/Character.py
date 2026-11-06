import sys
sys.path.insert(0, 'src (scripts for classes)/')

from dice import Dice
from items import Weapon


class Character:
    """Represents a character in the RPG"""
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None) -> None:
        """
        Initialise the Character
        Args:
        name (str): The name of the character.
        hp_max (int): Max hit points (default = 100)
        damage (int): Damage delt when character attacks (default = 10)
        weapon: optional weapon defined by the Weapon class
        """
        self.name = name
        self._hp = hp_max
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, target: Character) -> None:
        """Changes the character's hp based on the targets damage"""
        if target.weapon is None:
            self._hp -= target.damage
            self._hp = max(self._hp, 0)
        if isinstance(target.weapon, Weapon):
            self._hp -= target.weapon.roll_damage()
            self._hp = max(self._hp, 0)

    def heal(self, amount: int = 10) -> None:
        """Heals the character by a given amount"""
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)

    def attack(self, target: Character) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self)

    @property
    def is_alive(self) -> bool:
        """Checks if character hp is over or equal to zero"""
        if self._hp > 0:
            return True
        return False


aria = Character(name="Aria", hp_max=100, damage=10)
kura = Character(name="Kura", hp_max=100, damage=20)

print('starting hp:', aria._hp)
aria.take_damage(kura)
print('after 20 damage:', aria._hp)
aria.heal()
print('after 10 heal:', aria._hp)
kura.attack(aria)
print('after being attacked by kura:', aria._hp)
kura.attack(aria)
kura.attack(aria)
kura.attack(aria)
print('is aria alive?', aria.is_alive, 'hp:', aria._hp)
kura.attack(aria)
print('is aria alive?', aria.is_alive, 'hp:', aria._hp)


d8 = Dice(sides=8)
sword = Weapon(name='sword', damage_dice=d8)
swordsman = Character(name="swordsman", hp_max=100, weapon=sword)

print('-----------')
print('kura starting hp:', kura._hp)
swordsman.attack(kura)
print('hp after sword attack:', kura._hp)
