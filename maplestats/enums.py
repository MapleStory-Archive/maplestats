from enum import Enum, auto
from typing import Dict, Union


class ClassBranch(Enum):
    """Enum representing the five class branches."""
    WARRIOR = auto()
    MAGICIAN = auto()
    BOWMAN = auto()
    THIEF = auto()
    PIRATE = auto()


class CharClass(Enum):
    """Enum representing character classes."""
    BUCCANEER = auto()
    KAISER = auto()

    @property
    def branch(self) -> ClassBranch:
        """Returns the branch of this class."""
        return CLASS_TO_BRANCH[self]

    @classmethod
    def maybe_parse(cls, class_name: Union['CharClass', str]):
        if isinstance(class_name, CharClass):
            return class_name
        return cls[class_name.upper()]


CLASS_TO_BRANCH: Dict[CharClass, ClassBranch] = {
    CharClass.BUCCANEER: ClassBranch.PIRATE,
    CharClass.KAISER: ClassBranch.WARRIOR,
}
