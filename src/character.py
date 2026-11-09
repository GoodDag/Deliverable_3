from items import Weapon


class Character:
    """Represents a character in the RPG"""
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                  weapon: Weapon | None = None) -> None:
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
        if isinstance(target.weapon, Weapon):
            self._hp -= target.weapon.roll_damage()
            self._hp = max(self._hp, 0)
        else:
            self._hp -= target.damage
            self._hp = max(self._hp, 0)

    def take_mana_damage(self, target: Character) -> None:
        self._hp -= target.damage * 2
        self._hp = max(self._hp, 0)

    def heal(self, amount: int = 10) -> None:
        """Heals the character by a given amount"""
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)

    def attack(self, target: Character) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self)

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    @property
    def is_alive(self) -> bool:
        """Checks if character hp is over or equal to zero"""
        if self._hp > 0:
            return True
        return False

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe
        edits."""
        return self._hp

    def __repr__(self) -> str:
        """Representation of character object"""
        if isinstance(self.weapon, Weapon):
            return f"<Character name={self.name} hp={self.hp} weapon={self.weapon}>)"
        else:
            return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        if isinstance(self.weapon, Weapon):
            return f"Character: {self.name} with {self.hp} HP and d{self.weapon.damage_dice.sides} weapon damage"
        else:
            return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"


class Warrior(Character):
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                  weapon: Weapon | None = None, armor: int = 5) -> None:
        """
        Initialise the Character
        Args:
        armor (int): how much extra hp the armor gives to the warrior.
        """
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, target: Character) -> None:
        """Changes the hp based on if there is a weapon or not and damages the armor first"""
        if isinstance(target.weapon, Weapon):
            armor_damage = target.weapon.roll_damage() - self.armor
            self._hp = max(self._hp - max(armor_damage, 0), 0)
        else:
            self._hp -= max(target.damage - self.armor, 0)

    def take_mana_damage(self, target: Character) -> None:
        self._hp -= max(target.damage * 2 - self.armor, 0)
        self._hp = max(self._hp, 0)

    def __str__(self) -> str:
        """String representation of warrior object"""
        if isinstance(self.weapon, Weapon):
            return f"Warrior: {self.name} with {self.hp} HP, {self.armor} armor and d{self.weapon.damage_dice.sides} weapon damage"
        else:
            return f"Warrior: {self.name} with {self.hp} HP, {self.armor} armor and {self.damage} damage"


class Mage(Character):
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                 weapon: Weapon | None = None, mana: int = 30, mana_max: int = 30) -> None:
        """
        Initialise the Character
        Args:
        mana (int): how much mana the mage has with a defult of 30
        mana_max (int): max amount of mana the mage can have
        """
        super().__init__(name, hp_max, damage, weapon)
        self._mana = mana
        self.mana_max = mana_max

    def attack(self, target: Character) -> None:  
        """Removes 10 mana when used and adds 5 mana if it is under 10,
          if the mage have a weapon it will be used if the mana is under 10"""
        if self._mana >= 10:
            self._mana = self._mana - 10
            target.take_mana_damage(self)
        elif self._mana < 10:
            target.take_damage(self)
            self._mana = min(self._mana + 5, self.mana_max)

    def __str__(self) -> str:
        """String representation of mage object"""
        if isinstance(self.weapon, Weapon):
            return f"Mage: {self.name} with {self.hp} HP, {self._mana} mana and d{self.weapon.damage_dice.sides} weapon damage"
        else:
            return f"Mage: {self.name} with {self.hp} HP, {self._mana} mana and {self.damage} damage"
