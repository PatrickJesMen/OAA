# OOP project
from main import combat, generate

# Imports
from random import randint, choice
from os import system

# Test
HERO = generate.generate_hero()
combat.combat_loop(HERO)