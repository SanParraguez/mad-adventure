"""
=====================================================================
  Scenes / Gathering Berries
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option, chance_roll
from utils import sleep

# ===== Scene =======================================================

@register
def gathering_berries_scene():
    
    print(f"\nOh nice, some berries!")
    sleep(2.0)

    next_scene = choose_option([
        ('Gather them', continuation_scene),
        ('Ignore them', None)
    ])

    return next_scene

# -----------------------------------------------

def continuation_scene():
    
    print(f"\nThey look a little too delicious...")
    sleep(2.0)

    chance_of_death = chance_roll(10) # 10 percent probability of death
    
    if chance_of_death:
        
        print(f"\nI feel the urge to eat them")
        sleep(1.0)
        print(f"\nOh wow they are so delicious")
        sleep(1.0)
        print(f"\nI CAN'T STOP EATING")

        return False
    
    else:

        print(f"\nLet's leave them here")
        return None
