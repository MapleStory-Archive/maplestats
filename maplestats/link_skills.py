from abc import ABC, abstractmethod
from typing import Set

from maplestats.enums import Class
from maplestats.utils import STATS_TYPING


class LinkSkill(ABC):

    def __init__(self, level: int):
        self._level = level

    @abstractmethod
    def _classes(self) -> Set[Class]:
        raise NotImplementedError

    @abstractmethod
    def stats(self) -> STATS_TYPING:
        raise NotImplementedError

    @property
    def level(self):
        return self._level


class MagicianLink(LinkSkill):

    def _classes(self) -> Set[Class]:
        return {Class.IL_ARCHMAGE, Class.FP_ARCHMAGE, Class.BISHOP}

    def stats(self) -> STATS_TYPING:
        return {}


class ThiefLink(LinkSkill):

    def _classes(self) -> Set[Class]:
        return {Class.NIGHT_LORD, Class.SHADOWER, Class.DUAL_BLADE}

    def stats(self) -> STATS_TYPING:
        return {}
