"""
=====================================================================
  Scenes / Dragon Footprints Scene
=====================================================================
"""

# Imports
from ._registry import register 
from engine import choose_option, chance_roll
from utils import sleep

# ===================================================================

@register
def dragon_footprints_scene():
    
    print(f"\nWhat are those? They look huge...")
    sleep(2.0)
    print("They look like FOOTPRINTS!!", end=' ', flush=True)
    sleep(2.0)
    print(" But what kind of animal would have footprints this big?")
    sleep(1.0)
    next_scene = choose_option([
        ('follow the footprints', footprints_cont),
        ('ignore and walk the other way', None)
    ])

    return next_scene

def footprints_cont():
    
    print(f"\nMaybe it's something like a big bear...")
    sleep(1.0)
    print(f"Or a huge wolf...")
    sleep(1.0)
    print(f"wait what if it's a dragon!?")
    sleep(2.0)
    
    find_dragon = chance_roll(30)
    
    if find_dragon:
        
        print(f"\nWell the footprints seem to end h-OH NO! THE DRAGON! IT'S RIGHT THERE!")
        sleep(1.0)
        print(f"IT SAW ME!")
        sleep(1.0)
        print(f"It's running towards me...")
        sleep(1.0)
        print(f"AAAAAAAAAAAAAAAAAAAH")
        
        return False
    
    else:
        
        print(f"\nWell the footprints seem to end here")
        sleep(2.0)
        print(f"I guess the mystery will never be solved... time to keep walking")
        
        return None