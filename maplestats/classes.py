from abc import ABC, abstractmethod
from typing import Dict, Optional, Set, Tuple, Type

from maplestats.enums import Class, WeaponType


class CharacterClass(ABC):

    def __init__(self):
        self._enum: Optional[Class] = Class.get(
            self.__class__.__name__.upper())

    @abstractmethod
    def weapon(self) -> WeaponType:
        raise NotImplementedError

    @property
    def enum(self) -> Optional[Class]:
        return self._enum


class Beginner(CharacterClass):

    def weapon(self) -> WeaponType:
        return WeaponType.DAGGER


class Buccaneer(Beginner):

    def weapon(self) -> WeaponType:
        return WeaponType.KNUCKLE


_CLASSES: Set[Type[CharacterClass]] = {
    Beginner,
    Buccaneer,
}


def _generate_enum_to_class(classes: Set[Type[CharacterClass]]
                            ) -> Dict[Class, Type[CharacterClass]]:
    """Generates a mapping from Class enum to CharacterClass."""
    return {cls.enum: cls for cls in classes if cls.enum}


ENUM_TO_CLASS = _generate_enum_to_class(_CLASSES)
