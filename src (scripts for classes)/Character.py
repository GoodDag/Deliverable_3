class Character:
    """Represents a character in the RPG"""
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Initialise the Character
        Args:
        name (str): The name of the character.
        hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max
        self.hp_max = hp_max
        self.damage = damage

    def take_damage(self) -> None:
        self._hp -= self.damage   # Possibly change damage, not sure if correct
        self._hp = max(self._hp, 0)

    def heal(self, amount: int) -> None:
        self._hp += amount  # Same as damage, evaluate later
        self._hp = min(self._hp, self.hp_max)

    def attack(self, target: Character) -> None:
        """Attack and deal damage to target character"""
        target.take_damage()

    def is_alive(self) -> None:
        pass
