# Imports
from random import choice
from chars import enemy, hero

def generate_hero():
    hero_class = ['Warrior', 'Archer']
    hero_choice = choice(hero_class)

    match hero_choice:
        case 'Warrior':
            return hero.User('Warrior', 15, 70)
        case 'Archer':
            return hero.User('Archer', 24, 50)

def generate_monster():
    monsters_name = ['Goblin', 'Orc']
    monster = choice(monsters_name)

    match monster:
        case 'Goblin':
            return enemy.Enemy('Goblin', 10, 25)
        case 'Orc':
            return enemy.Enemy('Orc', 27, 60)
    