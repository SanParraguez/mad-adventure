"""
=====================================================================
  Scenes / Lake swimming
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option, chance_roll
from utils import sleep

# ===== Scene =======================================================

@register    # You need to register the entry scene of your arc (and add the module to the scenes.__init__.py file.
def example_scene():
    
    print(f"\nA beautiful LAKE appears...")
    sleep(2.0) # Add some suspense by adding breaks between text (this would add a 2 seconds break)
    print("...But is all frozen...", end=' ', flush=True)
    print(f"\n..ho noooorrrrr")
    sleep(2.0)
    print(f"\nBut wait, you see there is a whole in the middle of the lake")
    sleep(1.0)
    print(f"\nSince it is a sunny day you are deciding between:")

    # You can add options for the player to choose from like this:
    next_scene = choose_option([
        ('jumping in the lake', continuation_scene), # If you want option 1 to lead to a continuation_scene
        ('keep walking', None)                # If you want option 2 to exit this scene and continue the game
    ])

    return next_scene

# -----------------------------------------------

def continuation_scene():
    
    print(f"\n...fffffffhhhhhhh, the water is super cold...")
    sleep(1.0)

    example_roll = chance_roll(75) # You can use a chance roll like this, where 25 is the probability of success
    
    if example_roll:
        
        print(f"\nyou became an ice block and have to wait unitll spring before you are able to walk")
        sleep(1.0)

        return None
        # When you are ready to end the scene, return:
        #   None:  to continue the game
        #   True:  to win the game
        #   False: to lose the game
    
    else:

        return None
