"""
=====================================================================
  Testing utility
=====================================================================

Provides scene testing
"""

# Scenes
from scenes import SCENES_POOL


def testing(scenes):
    # scene pool is functions, make string list so it's searchable
    scene_names = {scene.__name__: scene for scene in SCENES_POOL}
    for scene in scenes:
        if scene in scene_names:
            print(f'Testing scene {scene} now:')
            scene_names[scene].__call__()
        else:
            print(f'\nWARNING There is no scene called {scene}')
    print('\nTesting concluded.')