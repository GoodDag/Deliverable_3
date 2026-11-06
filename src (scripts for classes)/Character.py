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

    def take_damage(self, target: Character) -> None:
        self._hp -= target.damage
        self._hp = max(self._hp, 0)

    def heal(self, amount: int = 10) -> None:
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)

    def attack(self, target: Character) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self)

    @property
    def is_alive(self) -> bool:
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