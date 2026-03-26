"""
=====================================================================
  Scenes / wounded_squirrel_scene
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option, chance_roll
from utils import sleep

# ===== Scene =======================================================

@register    # You need to register the entry scene of your arc (and add the module to the scenes.__init__.py file.
def example_scene():

    print(f"\nAs you wander, your gaze is met by a squirrel in your path")
    sleep(2.0) # Add some suspense by adding breaks between text (this would add a 2 seconds break)
   # print("There can also be a break in the same line", end=' ', flush=True)
    print(f"\nIt reciprocates your gaze with fearful eyes, glimmering with faint hope.")
    sleep(2.0)

    # You can add options for the player to choose from like this:
    next_scene = choose_option([
        ('You stop to help the squirrel', stop_to_help), # If you want option 1 to lead to a continuation_scene
        ('You continue, leaving the squirrel behind', None)                # If you want option 2 to exit this scene and continue the game
    ])

    return next_scene

# -----------------------------------------------

def stop_to_help():

    print(f"\nAs you crouch down to help the squirrel, you notice its back leg is dislocated")
    sleep(1.0)
    print(f"\nYou can try to help, but it will take a deft hand")
    sleep(1.0)
    print(f"\nThis could be risky...")
    fix_leg = choose_option([('I will try to fix his leg', dislocation_fix) ,("I'll carry him with me" , None)])
    return fix_leg



   # example_roll = chance_roll(25) # You can use a chance roll like this, where 25 is the probability of success

    #if example_roll:

       # print(f"\nThings are happening!")
        #sleep(1.0)

       # return None
        # When you are ready to end the scene, return:
        #   None:  to continue the game
        #   True:  to win the game
        #   False: to lose the game

   # else:
       # return None

def dislocation_fix():
	relocation_roll = chance_roll(50)
	if relocation_roll:
		print(f"\nPOP!")
		sleep(1.0)
		print(f"\n...")
		sleep(1.0)
		print(f"\nIt worked! the squirrels leg is fixed")
		print(f"\nThe squirrel leads you to safety!")
		return True
	else:
		print(f"\nPOP!")
		sleep(1.0)
		print(f"\n...oh no...")
		sleep(1.0)
		print(f"\his little leg broke from your force")
		return None

