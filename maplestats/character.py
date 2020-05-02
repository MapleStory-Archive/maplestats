import json
from typing import Any, Dict, Optional, Union

from maplestats.enums import (
    World, Stat, ClassBranch, Classes, EquipType, EMPTY_INVENTORY)
from maplestats.equipment import Equip
from maplestats.utils import STATS_TYPING, combine_stats


JOB_ADVANCEMENT_LEVEL_REQUIREMENTS = [10, 30, 60, 100, 200]


class Character:

    def __init__(
            self,
            name: str,
            level: int = 1,
            char_class: Union[Classes, str] = Classes.BEGINNER,
            world: World = None,
            equips: Dict[Union[EquipType, str], Optional[Equip]] = None,
            *args,
            **kwargs,
    ):
        del args
        del kwargs
        assert 1 <= level <= 275, 'Level must be between 1 and 275'

        self.name = name
        self.level = level
        self._char_class: Classes = Classes.maybe_parse(char_class)
        self._world = world
        self.equips = _maybe_parse_equips(equips)

        self._in_reboot = world.is_reboot if world else False
        self._main_stat: Stat = self._char_class.main_stat
        self._secondary_stat: Stat = self._char_class.secondary_stat

    @property
    def char_class(self) -> Classes:
        return self._char_class

    @char_class.setter
    def char_class(self, new_class: Classes):
        self._char_class: Classes = Classes.maybe_parse(new_class)
        self._main_stat = self._char_class.main_stat
        self._secondary_stat = self._char_class.secondary_stat

    @property
    def world(self) -> World:
        return self._world

    @world.setter
    def world(self, new_world: Optional[World]):
        self.world = new_world
        self._in_reboot = new_world.is_reboot if new_world else False

    @property
    def job(self) -> int:
        """Job of this character"""
        for idx, lvl_req in enumerate(JOB_ADVANCEMENT_LEVEL_REQUIREMENTS):
            if self.level < lvl_req:
                return idx + 1
        return 5

    @property
    def class_branch(self) -> ClassBranch:
        return self._char_class.branch

    @property
    def pure_main_stat(self) -> int:
        """Pure stat from leveling up"""
        stat = 5 * self.level + 4
        if self.job >= 4:
            return stat + 10
        if self.job == 3:
            return stat + 5
        return stat

    @property
    def pure_secondary_stat(self) -> int:
        return 4

    @property
    def damage(self) -> int:
        dmg = 50 if self._in_reboot else 0
        dmg += self.stats_from_equips[Stat.DMG]
        return dmg

    @property
    def stats_from_equips(self) -> STATS_TYPING:
        return combine_stats(equip.stats for equip in self.equips)

    def to_json(self, full: bool = False) -> Dict[str, Any]:
        """Returns the JSON representation of this character.

        Args:
            full: If True, includes all information about this character. If
                False, returns a minimal representation of this character.
        """
        minimal_repr = {
            'name': self.name,
            'level': self.level,
            'char_class': self._char_class,
            'world': self._world,
            'equips': self.equips,
        }
        if not full:
            return minimal_repr

        # Only data relevant to damage is included
        full_repr = {
            **minimal_repr,
            'pure_main_stat': self.pure_main_stat,
            'pure_secondary_stat': self.pure_secondary_stat,
        }

        # Convert classes and enums to strings
        for k, v in full_repr.items():
            if hasattr(v, "to_json"):
                full_repr[k] = v.to_json()
            elif isinstance(v, dict):
                new_v = {}
                for a, b in v.items():
                    new_a = a.to_json if hasattr(a, "to_json") else a
                    new_b = b.to_json if hasattr(b, "to_json") else b
                    new_v[new_a] = new_b
                full_repr[k] = new_v

        return full_repr

    def write_json(self, file_path: str = None) -> None:
        file_path = file_path if file_path else f'{self.name}.json'

        with open(file_path, 'w') as f:
            json.dump(self.to_json(), f)

    @classmethod
    def from_file(cls, file_path: str) -> 'Character':
        with open(file_path, 'r') as f:
            json_repr = json.load(f)
        return cls(**json_repr)


def _maybe_parse_equips(equips: Optional[Dict[Union[EquipType, str], Equip]]
                        ) -> Dict[EquipType, Optional[Equip]]:
    """Maybe parse equips."""
    if not equips or not isinstance(equips, dict):
        return EMPTY_INVENTORY

    return {EquipType.maybe_parse(equip_type): equip
            for equip_type, equip in equips.items()}
