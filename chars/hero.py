# OOP project

# Imports
from random import randint
from chars import character

# Colors
COLOR_RESET = '\033[0m'
COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[32m'
COLOR_YELLOW = '\033[93m'
COLOR_BLUE = '\033[94m'
COLOR_MAGENTA = '\033[95m'
COLOR_CYAN = '\033[96m'
COLOR_WHITE = '\033[97m'
COLOR_GRAY = '\033[90m'
COLOR_BOLD = '\033[1m'

# Class
class User(character):
    def __init__(self):
        super().__init__(
            name='',
            attack_damage=0,
            health=100,
            defense=0,
            agility=10,
            critical_chance=10,
            critical_attack_damage=50
        )


    def attack(self):
        is_critical = randint(1, 100) <= 20
        multiplier = 1.5 if is_critical else 1.0
        attack_damage_dealt = int(self._attack_damage * multiplier)
        return attack_damage_dealt, is_critical
    
    @property
    def hp(self):
        TOTAL_HP = self._max_hp
        HP = self._health
        TOTAL_BARS = 10

        full_bar = int((HP/TOTAL_HP) * TOTAL_BARS) 
        empty_bar = (TOTAL_BARS - full_bar)
        percentage = (HP/TOTAL_HP) * 100

        if percentage <= 25:
            color = COLOR_RED
        elif percentage <= 60:
            color = COLOR_YELLOW
        else:
            color = COLOR_GREEN

        DISPLAY_HP = full_bar * '█ '
        DISPLAY_LEFT_HP = empty_bar * '█ '

        return f'{color}{DISPLAY_HP}{COLOR_GRAY}{DISPLAY_LEFT_HP}{COLOR_RESET}'        
