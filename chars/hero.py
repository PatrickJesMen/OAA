# OOP project

# Imports
from random import randint
from chars.character import Character

# Class
class User(Character):
    def __init__(self, user_class: str, attack_damage: float, health: float):
        super().__init__(
            name=user_class,
            attack_damage=attack_damage,
            health=health,
            defense=10,
            agility=10,
            critical_chance=10,
            critical_attack_damage=50
        )

        self._user_class = user_class

        self._level = 1
        self._xp = 0
        self._xp_to_next_level = 100

    def gain_xp(self, amount: int):
        self._xp += amount
        print(f'\nYou gained {amount} XP!')

    def status(self):
        self._health += int((self._health/100)*10)
        self._attack_damage += int((self._attack_damage/100)*10)
        self._defense += int((self._defense/100)*10)
        self._agility += int((self._agility/100)*10)

    def level_up(self):
        self._xp -= self._xp_to_next_level
        self._level += 1
        self._xp_to_next_level = int(self._xp_to_next_level * 1.5)



    


    