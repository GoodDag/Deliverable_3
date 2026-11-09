from character import Character


class Battle:
    """Simulate a battle between two characters"""
    def __init__(self, hero: Character, enemy: Character):
        """
        Initialize the battle between two characters
        Args:
        hero (Character): sets a Character as the hero in the battle simulation
        enemy (Character): sets a Character as the enemy in the battle simulation
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Does one round of attacks between a hero and an enemy,
        as long as the enemy is alive after being attacked"""
        self.hero.attack(self.enemy)
        if self.enemy.is_alive is True:
            self.enemy.attack(self.hero)

    def simulate_battle(self, round: int = 1) -> str:
        """Simulates a battle between two characters as long as both of them are alive"""
        hero_starting_hp = self.hero.hp_max
        enemy_starting_hp = self.enemy.hp_max
        while self.hero.is_alive and self.enemy.is_alive is True:
            self.play_round()
            hero_damage = enemy_starting_hp - self.enemy.hp
            enemy_damage = hero_starting_hp - self.hero.hp
            print(f'Round {round}:')
            print(f'{self.hero.name} does {hero_damage} damage to {self.enemy.name}!')
            print(f'{self.enemy.name} does {enemy_damage} damage to {self.hero.name}!')
            print('-----')
            round += 1
            hero_starting_hp = self.hero.hp
            enemy_starting_hp = self.enemy.hp

        if self.hero.is_alive is False:
            print(f'{self.enemy.name} does {enemy_damage} damage to {self.hero.name}, reducing their hp to 0!')
            return f'{self.hero.name} is dead, {self.enemy.name} has won with {self.enemy.hp} hp left!'
        else:
            print(f'{self.hero.name} does {hero_damage} damage to {self.enemy.name}, reducing their hp to 0!')
            return f'{self.enemy.name} is dead, {self.hero.name} has won with {self.hero.hp} hp left!'
