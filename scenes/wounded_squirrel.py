"""
=====================================================================
  Scenes / Name of your scene
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option, chance_roll
from utils import sleep

# ===== Scene =======================================================

@register    # You need to register the entry scene of your arc (and add the module to the scenes.__init__.py file.
def getting_late():
    
    print(f"\nThe sun has begun to set...")
    sleep(1.0)
    print(f"\nYou feel tired and start looking for a place to rest.")

    # You can add options for the player to choose from like this:
    next_scene = choose_option([
        ('Look for a tree', tree_scene), # If you want option 1 to lead to a continuation_scene
        ('Look for a cave', cave_scene)                # If you want option 2 to exit this scene and continue the game
    ])

    return next_scene

# -----------------------------------------------

def tree_scene():
    
    print(f"\nYou look for a suitably protected place within the forest...")
    sleep(1.0)

    found_tree = chance_roll(25) # You can use a chance roll like this, where 25 is the probability of success
    
    if found_tree:
        
        print(f"\nYou find a small secluded grove.")
        sleep(1.0)
        print(f"\nAs you begin to make your bedroll, you hear a small noise...")

        next_scene = choose_option([
            ('Investigate the sound', squirrel_scene)
            ('Ignore the sound', monster_scene)
	])

        return next_scene
    
    else:

        print(f"\nYou can't find a good place.")
        next_scene = choose_option([
            ('Continue looking for a tree', monster_scene)
	    ('Switch to looking for a cave', cave_scene)
        ])

    return next_scene

# -----------------------------------------------

def cave_scene():
    
    print(f"\nYou look for a suitably protected cave...")
    sleep(2.0)
    print(f"\nYou find the perfect looking cave.")
    sleep(1.0)
    print(f"\nAs you are about to enter, you hear a small noise by a tree.")

    next_scene = choose_option([
        ('Check it out the noise', squirrel_scene), # If you want option 1 to lead to a continuation_scene
        ('Ignore', monster_scene)                # If you want option 2 to exit this scene and continue the game
    ])

    return next_scene

# -----------------------------------------------

def monster_scene():

    print(f"\nYou feel safe within your warm bedroll.", ' ', flush=True)
    sleep(1.0)
    print(f".", ' ', flush=True)
    sleep(1.0)
    print(f".", ' ', flush=True)
    sleep(2.0)
    print(f"\nAs you're about to drift to sleep, you hear a strange noise.")
    sleep(1.0)
    print(f"\nYou open you eyes, yet it is still dark.")
    sleep(1.0)
    print(f"\nYour head is filled with questions, as you lose consciousness,", ' ', flush=True)
    sleep(1.0)
    print(f"wondering...", ' ', flush=True)
    sleep(1.0)
    print(f"\nWhat did I do wrong?")

    return False

# -----------------------------------------------

def squirrel_scene():

    print(f"\nFollowing the noise, you find a small, cute wounded squirrel")

    return True # For now just to debug
