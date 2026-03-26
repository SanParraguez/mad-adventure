"""
=====================================================================
  Scenes / Scarf Scene
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option, chance_roll
from utils import sleep

@register
def scarf_scene():
    
    print(f"\nA SCARF...")
    sleep(2.0)
    print("Somehow it feels familiar...")
    sleep(1.0)

    next_scene = choose_option([
        ('take the scarf', scarf_taken),
        ('ignore it and keep walking', None)
    ])

    return next_scene

def scarf_taken():
    
    print(f"This scarf feels so familiar...")
    sleep(1.0)
    print(f"The scent... I can almost remember...")
    sleep(1.0)
    find_friend = chance_roll(30)
    
    if find_friend:
        
        print(f"\nThere's someone over there!")
        sleep(1.0)
        print(f"They look so familiar...")
        sleep(1.0)
        print(f"MY FRIEND! WAIT! I REMEMBER YOU NOW! I REMEMBER EVERYTHING!")
        sleep(1.0)        
        return True
    
    else:
        
        print(f"\nI can't reach the memory but I think it was a good one")
        sleep(1.0) 
        print(f"\nI feel like this scarf will protect me...")
        sleep(1.0)
        print(f"I can keep going now")
        sleep(1.0)
        return None