"""
=====================================================================
  Scenes / Dark Forest Scene
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option, chance_roll
from utils import sleep

# ===== Scene =======================================================

@register 
def dark_forest_scene():
    
    print(f"\nThis path is getting a little bit monotonous now")
    sleep(2.0) 
    print("Should I change path to see what else I discover?")
    sleep(2.0)
    print("Let's see... ", end=' ', flush=True)
    sleep(2.0)
    print("There is a similar road to the right and a denser forest to the left, what should I do?")
    sleep(2.0)

    next_scene = choose_option([
        ('go into the forest', entering_forest_scene),
        ('take the path on the right', right_path_scene),
        ('stay on the same road', None)
    ])

    return next_scene

# -----------------------------------------------


def entering_forest_scene():
    
    sleep(1.0)
    print(f"\nOk yes I'll go in. I'm not scared")  
    sleep(3.0)
    print("Well I will not lie, maybe I am a little bit scared...")
    
    next_scene = choose_option([
        ('continue entering the forest', inside_forest_scene),
        ('turn around', right_path_scene)
    ])
    
    return next_scene  

def inside_forest_scene():
    
    sleep(1.0)
    print(f"\nThis is slightly spooky...")
    sleep(2.0)
    print("It is so dark in here I can barely see my own feet...")
    sleep(2.0)
    print("Wait, where am I?")
    sleep(2.0)
    print("Wait... ", end=' ', flush=True)
    sleep(2.0)
    print("how did I get here?")
    sleep(2.0)
    print("Oh, a forest! Let's go in")
    sleep(2.0)

    return entering_forest_scene

def right_path_scene():
    
    sleep(1.0)
    print(f"\nYes the forest looked a little bit scary")
    sleep(1.0)
    print("This is better")
    sleep(2.0)
    
    return None