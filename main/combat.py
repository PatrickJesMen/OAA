# Imports
from random import randint
from os import system
from main import generate
from chars import enemy, hero

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

def clear():
    system('cls')

def combat_loop(HERO):
    proceed = True
    while proceed:
        clear()
        MONSTER = generate.generate_monster()

        print(f"A wild {COLOR_RED}{MONSTER._name}{COLOR_RESET} spawned! What you want to do?")
        
        choice = input("1. FIGHT\n2. RUN\n")
        if choice == '1':
            proceed = False
        else:
            print("\nYou ran away, but another monster approaches...")
            input("Press Enter to continue...")
            continue
    
    while HERO._health > 0 and MONSTER._health > 0:
        clear()
        print(f"{COLOR_GRAY}════════════════════════════════════════{COLOR_RESET}")
        print(f" 🦸 CHARACTER: {COLOR_GREEN}{HERO._user_class:<24}{COLOR_RESET} ")
        print(f"{COLOR_GRAY}════════════════════════════════════════{COLOR_RESET}")
        print(f"❤️  HP: {HERO._health} ║ {HERO.hp}")
        print(f"⚔️  DAMAGE: {HERO._damage:<25}")
        print(f"{COLOR_GRAY}════════════════════════════════════════{COLOR_RESET}")
        
        # Separator
        print("\n      ⟡ ══════════ VS ══════════ ⟡      \n")
        
        # Displaying Enemy Stats
        print(f"{COLOR_GRAY}════════════════════════════════════════{COLOR_RESET}")
        print(f" 👹 CHARACTER:{COLOR_RED} {MONSTER._name:<24}{COLOR_RESET} ")
        print(f"{COLOR_GRAY}════════════════════════════════════════{COLOR_RESET}")
        print(f" ❤️  HP: {MONSTER._health} ║ {MONSTER.hp} ")
        print(f" 🗡️  DAMAGE: {MONSTER._damage:<25} ")
        print(f"{COLOR_GRAY}════════════════════════════════════════{COLOR_RESET}")

        action = input("\n[1] Attack\n> ")
        if action == '1':
            damage, is_critical = HERO.attack()

            if is_critical: 
                print(f'\n{COLOR_YELLOW}💥CRITICAL HIT!{COLOR_RESET} You attack the {MONSTER._name} for {damage} damage!')
            else:
                print(f"\nYou attack the {MONSTER._name} for {damage} damage!")

            MONSTER._health -= damage

        if MONSTER._health <= 0:
            print(f"You defeated the {MONSTER._name}!")
            break
            
        # Enemy's Turn
        damage, is_critical = MONSTER.attack()

        if is_critical:
            print(f'\n{COLOR_YELLOW}💥CRITICAL HIT!{COLOR_RESET} The {MONSTER._name} attacks you for {damage} damage!')
        else:
            print(f"The {MONSTER._name} attacks you for {damage} damage!")
        

        HERO._health -= damage
        
        if HERO._health <= 0:
            print("You have been defeated...")
            break
            
        input("\nPress Enter for the next turn...")
