"""
Utility for easily restoring a working session. The last modified character is
loaded into a local variable `me: Character`. Useful enums and functions are
also imported.

This module is intended to be imported into a console with:
    from maplestats.session import *
"""
from maplestats.session_utils import load_last_modified

# Useful enums
# pylint: disable=unused-import
from maplestats.enums import World, Stat, Class, EquipType, WeaponType


me = load_last_modified()
if me:
    print(f'Welcome, {me.name}!')
