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
def example_scene():
    
    print(f"\nYou can write some text like this")
    sleep(2.0) # Add some suspense by adding breaks between text (this would add a 2 seconds break)
    print("There can also be a break in the same line", end=' ', flush=True)
    sleep(2.0)
    print("like this!")
    sleep(1.0)

    # You can add options for the player to choose from like this:
    next_scene = choose_option([
        ('option 1', continuation_scene), # If you want option 1 to lead to a continuation_scene
        ('option 2', None)                # If you want option 2 to exit this scene and continue the game
    ])

    return next_scene

# -----------------------------------------------

def continuation_scene():
    
    print(f"\nThis is an example continuation scene")
    sleep(1.0)

    example_roll = chance_roll(25) # You can use a chance roll like this, where 25 is the probability of success
    
    if example_roll:
        
        print(f"\nThings are happening!")
        sleep(1.0)

        return None
        # When you are ready to end the scene, return:
        #   None:  to continue the game
        #   True:  to win the game
        #   False: to lose the game
    
    else:

        return None