"""
=====================================================================
  Scenes / Castle
=====================================================================
"""
# Imports
from random import randint
# Core imports
from ._registry import register
from engine import choose_option, chance_roll
from utils import sleep

# ===== Scene =======================================================

@register
def castle_scene():
    
    print(f"\nThere seems to be a building over there... It's a CASTLE!")
    sleep(2.0)
    print("It looks so beautiful")
    sleep(1.0)
    next_scene = choose_option([
        ('enter the castle', castle_cont),
        ('ignore and walk the other way', None)
    ])

    return next_scene

def castle_cont():
    
    print(f"\nIt is very dark in here")
    sleep(1.0)
    print(f"The ceilings are so tall... but barely any light is coming in")
    sleep(1.0)
    print(f"Where should I go?")
    sleep(1.0)
    next_scene = choose_option([
        ('go up the stairs', castle_up),
        ('go to the right', castle_right),
        ('go to the left', castle_left),
        ('leave the castle', None)
    ])
    
    return next_scene
    
def castle_up():
    
    print(f"\nEverything looks very dusty...")
    sleep(1.0)
    print(f"I wonder who used to live here...")
    sleep(1.0)
    find_dragon = chance_roll(20)
    
    if find_dragon:
        print(f"\nOH NO! A DRAGON!")
        sleep(1.0)
        print(f"IT SAW ME!")
        sleep(1.0)
        print(f"It's running towards me...")
        sleep(1.0)
        print(f"AAAAAAAAAAAAAAAAAAAH")
        
        return False
    
    else:
        print(f"\nWell there seems to be nothing over here, apart from all this dust")
        sleep(1.0)
        print(f"I guess I'll go back outside")
        
        return None
    
def castle_right():
    
    print(f"\nThis castle looks very old")
    sleep(1.0)
    print(f"\nI wonder when was the last time someone stepped foot here...")
    find_skeleton = chance_roll(30)
    
    if find_skeleton:
        print(f"\nAAAAAAHH! A SKELETON!")
        sleep(1.0)
        print(f"RUN RUN RUN")
        sleep(2.0)
        print(f"That was so scary... I'm not going back inside that castle")
        
        return None
    
    else:
        print(f"\nThere seems to be nothing over here, apart from all this dust")
        sleep(1.0)
        print(f"I guess I'll go back outside")
        
        return None
    
def castle_left():
    
    print(f"\nThis castle looks very old")
    sleep(1.0)
    print(f"\nI wonder when was the last time someone stepped foot here...")
    find_food = randint(0, 100)
    
    if find_food > 20:
        print(f"\nA huge table full of food!")
        sleep(1.0)
        print(f"I am so hungry...")
        sleep(1.0)
        next_scene = choose_option([
            ('eat the food', castle_foodpoisoning),
            ('ignore the food and go back outside', None)
        ])
        return None
    
    else:
        print(f"\nThere seems to be nothing over here, apart from all this dust")
        sleep(1.0)
        print(f"I guess I'll go back outside")
        
        return None
    
def castle_foodpoisoning():
    
    print(f"\nI don't feel so good...")
    sleep(1.0)
    print(f"I think I might throw up...")
    sleep(5.0)
    print(f"Well that was a bad decision")
    sleep(1.0)
    print(f"I'd better go back outside")
    
    return None
    