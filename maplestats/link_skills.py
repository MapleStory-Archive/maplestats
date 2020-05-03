from abc import ABC, abstractmethod
from typing import Dict, Set, Type

from maplestats.enums import Class, Stat
from maplestats.utils import STATS_TYPING


class LinkSkill(ABC):

    def __init__(self, level: int):
        assert 1 <= level <= self._max_level
        self._level = level

    @abstractmethod
    @property
    def classes(self) -> Set[Class]:
        raise NotImplementedError

    @abstractmethod
    def stats(self) -> STATS_TYPING:
        raise NotImplementedError

    @property
    @abstractmethod
    def _max_level(self) -> int:
        raise NotImplementedError

    @property
    def level(self):
        return self._level


class MagicianLink(LinkSkill):

    def classes(self) -> Set[Class]:
        return {Class.IL_ARCHMAGE, Class.FP_ARCHMAGE, Class.BISHOP}

    def _max_level(self) -> int:
        return 6

    def stats(self) -> STATS_TYPING:
        return {}


class ThiefLink(LinkSkill):

    def classes(self) -> Set[Class]:
        return {Class.NIGHT_LORD, Class.SHADOWER, Class.DUAL_BLADE}

    def _max_level(self) -> int:
        return 6

    def stats(self) -> STATS_TYPING:
        return {}


class PirateLink(LinkSkill):

    def classes(self) -> Set[Class]:
        return {Class.BUCCANEER, Class.CORSAIR, Class.CANNON_MASTER}

    def _max_level(self) -> int:
        return 6

    def stats(self) -> STATS_TYPING:
        return {Stat.ALL: 10 * self.level + 10}


class ResistanceLink(LinkSkill):

    def classes(self) -> Set[Class]:
        return {
            Class.WILD_HUNTER, Class.MECHANIC, Class.BATTLE_MAGE, Class.BLASTER}

    def _max_level(self) -> int:
        return 8

    def stats(self) -> STATS_TYPING:
        return {}


class DSLink(LinkSkill):

    def classes(self) -> Set[Class]:
        return {Class.DEMON_AVENGER}

    def _max_level(self) -> int:
        return 3

    def stats(self) -> STATS_TYPING:
        return {Stat.BOSS: 5 * self.level}


class DALink(LinkSkill):

    def classes(self) -> Set[Class]:
        return {Class.DEMON_AVENGER}

    def _max_level(self) -> int:
        return 3

    def stats(self) -> STATS_TYPING:
        return {Stat.DMG: 5 * self.level}


class BTLink(LinkSkill):

    def classes(self) -> Set[Class]:
        return {Class.BEAST_TAMER}

    def _max_level(self) -> int:
        return 3

    def stats(self) -> STATS_TYPING:
        return {Stat.BOSS: 3 * self.level + 1,
                Stat.CRIT: 3 * self.level + 1}


class ABLink(LinkSkill):

    def classes(self) -> Set[Class]:
        return {Class.ANGELIC_BUSTER}

    def _max_level(self) -> int:
        return 3

    def stats(self) -> STATS_TYPING:
        return {}


class ArkLink(LinkSkill):

    def classes(self) -> Set[Class]:
        return {Class.ARK}

    def _max_level(self) -> int:
        return 2

    def stats(self) -> STATS_TYPING:
        return {Stat.DMG: 5 * self.level + 1}


class CadenaLink(LinkSkill):

    def classes(self) -> Set[Class]:
        return {Class.CADENA}

    def _max_level(self) -> int:
        return 2

    def stats(self) -> STATS_TYPING:
        return {Stat.DMG: 6 * self.level}


class KinesisLink(LinkSkill):

    def classes(self) -> Set[Class]:
        return {Class.KINESIS}

    def _max_level(self) -> int:
        return 2

    def stats(self) -> STATS_TYPING:
        return {Stat.CRIT_DMG: 2 * self.level}


class KannaLink(LinkSkill):

    def classes(self) -> Set[Class]:
        return {Class.KANNA}

    def _max_level(self) -> int:
        return 2

    def stats(self) -> STATS_TYPING:
        return {Stat.DMG: 5 * self.level}


_LINK_SKILLS: Set[Type[LinkSkill]] = {
    MagicianLink,
    ThiefLink,
    PirateLink,
    ResistanceLink,
    DSLink,
    DALink,
    BTLink,
    ABLink,
    ArkLink,
    CadenaLink,
    KinesisLink,
    KannaLink,
}


def _generate_class_to_link(link_skills: Set[Type[LinkSkill]]
                            ) -> Dict[Class, Type[LinkSkill]]:
    """Generates a mapping from Class enum to CharacterClass."""
    return {cls: link for link in link_skills for cls in link.classes}


CLASS_TO_LINK = _generate_class_to_link(_LINK_SKILLS)
