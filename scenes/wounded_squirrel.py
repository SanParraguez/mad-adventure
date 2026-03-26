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
#    sleep(2.0) # Add some suspense by adding breaks between text (this would add a 2 seconds break)
#    print("There can also be a break in the same line", end=' ', flush=True)
#    sleep(2.0)
#    print("like this!")
#    sleep(1.0)

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

	next_scene = found_squirrel

        return next_scene
        # When you are ready to end the scene, return:
        #   None:  to continue the game
        #   True:  to win the game
        #   False: to lose the game
    
    else:

	print(f"\nYou can't find a good place.")
	next_scene = choose_option([
		('Continue looking for a tree', monster_scene)
		('Switch to looking for a cave', cave_scene)
	])

	return next_scene
