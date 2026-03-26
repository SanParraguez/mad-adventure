"""
=====================================================================
  Scenes / fountain_scene 
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option, chance_roll
from utils import sleep

# ===== Scene =======================================================

@register    # You need to register the entry scene of your arc (and add the module to the scenes.__init__.py file.
def fountain_scene():
    
    print(f"\nYou reached a fountain...", end=" ", flush=True)
    sleep(2.0) 
    print("and it has water!")
    sleep(1.0)

    # You can add options for the player to choose from like this:
    next_scene = choose_option([
        ('Drink water', drink_water), 
        ('Leave', None)               
    ])

    return next_scene

# -----------------------------------------------

def drink_water():
    
    print(f"\nYou drink some water.")
    sleep(1.0)

    water_clean = chance_roll(90) 
    
    if water_clean:
        
        print(f"\nYou feel refreshed!")
        sleep(1.0)

        return None
    
    else:
        print(f"\nThe water tastes funny...")
        sleep(1.0)
        print(f"You don't feel well...", end=" ", flush=True)
        sleep(2.0)
        print(f"the water is poisonous!")
        sleep(2.0)
        print(f"Your eyes fade out...")

        return False
