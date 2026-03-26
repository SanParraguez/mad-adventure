"""
=====================================================================
  Scenes / Very Cool Stick
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option
from utils import sleep

# ===== Scene =======================================================

@register
def very_cool_stick_scene():

    print(f"\nOh wow! Down there! A very cool STICK!")
    sleep(1.0)
    print("I almost stepped on it...")
    sleep(1.0)
    print("Should I keep it to help me walk?")
    sleep(1.0)

    next_scene = choose_option([
        ('pick up the stick', found_snake),
        ('ignore it and keep walking', None)
    ])

    return next_scene

# -----------------------------------------------

def found_snake():

    sleep(1.0)
    print(f"\nAAAAAAH! A SNAKE!!")
    sleep(2.0)
    print(f"I hope it was not venomous... thankfully I managed to run away...")
    sleep(1.0)

    next_scene = None

    return next_scene
