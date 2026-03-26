"""
=====================================================================
  Scenes / Gathering berries
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option
from utils import sleep

# ===== Scene =======================================================

@register
def gathering_berries_scene():

    print(f"\nOh! there are blue berries tree!", end=' ', flush=True)
    sleep(2.0)
    print("I like blue berries cake")
    sleep(1.0)
    print("But the trees are in a private forest")
    sleep(2.0)
    

    next_scene = choose_option([
        ('pick blue berries up', pick_berries),
        ('keep walking', None)
    ])

    return next_scene

# -----------------------------------------------

def pick_berries():
    print("\n I cannot stop picking them up. They are looked too pretty", end=" ", flush=True)
    sleep(1.0)
    print("The forest owner finds me..."WHAT ARE YOU DOING HERE!! ")
    sleep(1.0)
    print("I run away with the full bag of blue berries")

    return None

# -----------------------------------------------
