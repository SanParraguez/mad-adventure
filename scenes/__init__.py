"""
=====================================================================
  Scenes
=====================================================================

To make a scene available you should import it here.

When adding the @registry decorator to a scene, that scene will be
automatically included into the pool of possible random scenes to
get in the game loop.
"""

from scenes._registry import SCENES_POOL

# IMPORT SCENE MODULES HERE
from . import flower_seller
from . import forest_gnomes
from . import very_cool_stick
from . import fun_mushrooms
from . import dark_forest
from . import castle
from . import dragon_footprints
from . import scarf
from . import gathering_berries
from . import fountain_scene
