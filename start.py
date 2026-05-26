# OOP project

# Imports
from main import combat, generate, status
from random import randint, choice
from os import system

# Test
hero_stats = status.status("hero")
enemy_stats = status.status("enemy")

print("Hero Stats:", hero_stats)
print("Enemy Stats:", enemy_stats)
