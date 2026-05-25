# █

def health():
    MAX_HP = 100 # each bar it's 10 hp
    HP = 100
    TOTAL_BARS = 10

    full_bar = int((HP/MAX_HP) * TOTAL_BARS) 
    empty_bar = (TOTAL_BARS - full_bar)
    percentage = (HP/MAX_HP) * 100

    if percentage <= 25:
        color = '\033[91m'
    elif percentage <= 60:
        color = '\033[93m'
    else:
        color = '\033[32m'

    DISPLAY_HP = full_bar * '█ '
    DISPLAY_LEFT_HP = empty_bar * '█ '

    return f'{color}{DISPLAY_HP}\033[90m{DISPLAY_LEFT_HP}\033[0m'

print(health())

