import json
from typing import Any, Dict, Optional, Union

from maplestats.enums import (
    World, Stat, JobBranch, Class, EquipType, EMPTY_INVENTORY)
from maplestats.equipment import Equip
from maplestats.utils import STATS_TYPING, combine_stats, jsonify, parse_json

JOB_ADVANCEMENT_LEVEL_REQUIREMENTS = [10, 30, 60, 100, 200]

LAST_MODIFIED_FILE_NAME = ".lastmodified"


class Character:

    def __init__(
            self,
            name: str,
            level: int = 1,
            character_class: Union[Class, str] = Class.BEGINNER,
            world: World = None,
            link_skills: Dict[Union[Class, str], int] = None,
            equips: Dict[Union[EquipType, str],
                         Optional[Union[Equip, Dict]]] = None,
            *args,
            **kwargs,
    ):
        del args
        del kwargs
        assert 1 <= level <= 275, 'Level must be between 1 and 275'

        self.name = name
        self.level = level
        self._character_class: Class = Class.maybe_parse(character_class)
        self._world = world
        self.link_skills = parse_json(link_skills, key_class=Class
                                      ) if link_skills else {}
        self.equips = parse_json(equips, key_class=EquipType, value_class=Equip
                                 ) if equips else EMPTY_INVENTORY

        self._in_reboot = world.is_reboot if world else False
        self._main_stat: Stat = self._character_class.main_stat
        self._secondary_stat: Stat = self._character_class.secondary_stat

    @classmethod
    def from_file(cls, file_path: str) -> 'Character':
        with open(file_path, 'r') as f:
            json_repr = json.load(f)
        return cls(**json_repr)

    @property
    def char_class(self) -> Class:
        return self._character_class

    @char_class.setter
    def char_class(self, new_class: Class):
        self._character_class: Class = Class.maybe_parse(new_class)
        self._main_stat = self._character_class.main_stat
        self._secondary_stat = self._character_class.secondary_stat

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
    def class_branch(self) -> JobBranch:
        return self._character_class.branch

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
        return combine_stats(equip.stats for equip in self.equips.values()
                             if equip is not None)

    def equip(self, equip: Equip) -> Optional[Equip]:
        """Equip an item and return the unequipped item."""
        equip_type = equip.equip_type
        unequipped = self.equips[equip_type]
        self.equips[equip_type] = equip
        return unequipped

    def to_json(self, full: bool = False) -> Dict[str, Any]:
        """Returns the JSON representation of this character.

        Args:
            full: If True, includes all information about this character. If
                False, returns a minimal representation of this character.
        """
        json_repr = {
            'name': self.name,
            'level': self.level,
            'character_class': self._character_class,
            'world': self._world,
            'equips': self.equips,
        }
        if full:
            # Only data relevant to damage is included
            json_repr.update({
                'pure_main_stat': self.pure_main_stat,
                'pure_secondary_stat': self.pure_secondary_stat,
            })

        return jsonify(json_repr)

    def save(self, file_path: str = None) -> None:
        file_path = file_path if file_path else f'{self.name}.json'

        with open(file_path, 'w') as f:
            json.dump(self.to_json(), f)

        _write_last_modified(file_path)


def _write_last_modified(file_path: str) -> None:
    with open(LAST_MODIFIED_FILE_NAME, 'w') as f:
        f.write(file_path)
