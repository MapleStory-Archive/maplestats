from abc import ABC, abstractmethod
from typing import Dict, Optional, Set, Tuple, Type

from maplestats.enums import Classes, WeaponType


class CharacterClass(ABC):

    def __init__(self):
        self._enum: Optional[Classes] = Classes.get(
            self.__class__.__name__.upper())

    @abstractmethod
    def weapon(self) -> WeaponType:
        raise NotImplementedError

    @property
    def enum(self) -> Optional[Classes]:
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


def _generate_class_enum_mappings(classes: Set[Type[CharacterClass]]
                                  ) -> Tuple[Dict, Dict]:
    """Generates a mapping from CharClass enum to AbstractCharClass and vice
    versa.
    """
    class_to_enum: Dict[Type[CharacterClass], Classes] = {}
    enum_to_class: Dict[Classes, Type[CharacterClass]] = {}

    for cls in classes:
        if cls.enum:
            class_to_enum[cls] = cls.enum
            enum_to_class[cls.enum] = cls

    return class_to_enum, enum_to_class


CLASS_TO_ENUM, ENUM_TO_CLASS = _generate_class_enum_mappings(_CLASSES)
