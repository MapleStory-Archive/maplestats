from abc import ABC, abstractmethod
from typing import Dict, Optional, Set, Tuple, Type

from maplestats.enums import CharClass, WeaponType


class AbstractCharClass(ABC):

    def __init__(self):
        self._enum: Optional[CharClass] = CharClass.get(
            self.__class__.__name__.upper())

    @abstractmethod
    def weapon(self) -> WeaponType:
        raise NotImplementedError

    @property
    def enum(self) -> Optional[CharClass]:
        return self._enum


class Buccaneer(AbstractCharClass):

    def weapon(self) -> WeaponType:
        return WeaponType.KNUCKLE


_CHARCLASS_ABCS: Set[Type[AbstractCharClass]] = {
    Buccaneer,
}


def _generate_enum_abc_mappings(abcs: Set[Type[AbstractCharClass]]
                                ) -> Tuple[Dict, Dict]:
    """Generates a mapping from CharClass enum to AbstractCharClass and vice
    versa.
    """
    abc_to_enum: Dict[Type[AbstractCharClass], CharClass] = {}
    enum_to_abc: Dict[CharClass, Type[AbstractCharClass]] = {}

    for abc in abcs:
        if abc.enum:
            abc_to_enum[abc] = abc.enum
            enum_to_abc[abc.enum] = abc

    return abc_to_enum, enum_to_abc


CHARCLASS_ABC_TO_ENUM, CHARCLASS_ENUM_TO_ABC = (
    _generate_enum_abc_mappings(_CHARCLASS_ABCS))
