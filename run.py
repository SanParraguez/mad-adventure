"""
=====================================================================
  Mad Adventure Game
=====================================================================
"""

# Imports
import random
import argparse
from config import settings
from utils import sleep

# Scenes
from scenes import SCENES_POOL
from scenes.wake_up import wake_up_scene


# === Parse arguments ===============================================

parser = argparse.ArgumentParser()
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()

settings.DEBUG = args.debug


# === Game loop =====================================================

def main():

    # Get the available scenes for the game
    max_scenes = len(SCENES_POOL)
    game_scenes = random.sample(SCENES_POOL, max_scenes)

    # Initialize game
    lives_counter = 3
    wake_up_scene()
    current_scene = game_scenes.pop(0)

    # Loop over scenes
    counter = 0
    while counter < max_scenes:

        current_scene = current_scene()

        if current_scene is False:
            lives_counter -= 1
            print("\nLife is fleeting...")
            if lives_counter < 1:
                sleep(1.0)
                print("\n...")
                sleep(1.0)
                print("\n...")
                sleep(1.0)
                print("\nTurns out that killed you.")
                break
            current_scene = None

        if current_scene is None and len(game_scenes) == 0:
            sleep(2.0)
            print("\nIt has been a long day, I should go back home now...")
            sleep(1.0)
            print("I just keep walking towards the sunset...")
            sleep(3.0)
            print("\nTo be continued...")
            break

        elif current_scene is None:
            sleep(2.0)
            print("\nI continue following the path...")
            sleep(1.0)
            current_scene = game_scenes.pop(0)
            counter += 1

        elif current_scene is True:
            print(f"\nCongratulations, you won!")
            break

    sleep(1.0)
    print("\n=====  The End  =====")


# === Run ===========================================================

if __name__ == "__main__":
    main()
