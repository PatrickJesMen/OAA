# OOP project

# Imports
from random import randint

class Enemy():
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
        
