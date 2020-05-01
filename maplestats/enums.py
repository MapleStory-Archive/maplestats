from enum import Enum, auto
from typing import Dict, Union, Set


class Stat(Enum):
    """Enum representing all types of stats."""
    ALL = auto()
    STR = auto()
    DEX = auto()
    INT = auto()
    LUK = auto()
    ATT = auto()
    MATT = auto()
    PCT_ALL = auto()
    PCT_STR = auto()
    PCT_DEX = auto()
    PCT_INT = auto()
    PCT_LUK = auto()
    PCT_ATT = auto()
    PCT_MATT = auto()
    BOSS = auto()
    IED = auto()
    CRIT = auto()
    CRIT_DMG = auto()
    FLAT_DMG = auto()


class ClassBranch(Enum):
    """Enum representing the five class branches."""
    BEGINNER = auto()
    WARRIOR = auto()
    MAGICIAN = auto()
    BOWMAN = auto()
    THIEF = auto()
    PIRATE = auto()


class CharClass(Enum):
    """Enum representing character classes."""
    BEGINNER = auto()
    ARAN = auto()
    EVAN = auto()
    MERCEDES = auto()
    PHANTOM = auto()
    SHADE = auto()
    LUMINOUS = auto()
    BOWMASTER = auto()
    MARKSMAN = auto()
    PATHFINDER = auto()
    BUCCANEER = auto()
    CORSAIR = auto()
    CANNON_MASTER = auto()
    JETT = auto()
    BEAST_TAMER = auto()
    DAWN_WARRIOR = auto()
    BLAZE_WIZARD = auto()
    WIND_ARCHER = auto()
    NIGHT_WALKER = auto()
    THUNDER_BREAKER = auto()
    KAISER = auto()
    ANGELIC_BUSTER = auto()
    ARK = auto()
    ILIUM = auto()
    ADELE = auto()

    @property
    def branch(self) -> ClassBranch:
        """Returns the branch of this class."""
        return CLASS_TO_BRANCH[self]

    @classmethod
    def maybe_parse(cls, class_name: Union['CharClass', str]):
        if isinstance(class_name, CharClass):
            return class_name
        return cls[class_name.upper()]

    @property
    def main_stat(self) -> Stat:
        if self.branch == ClassBranch.MAGICIAN:
            return Stat.INT
        if self.branch == ClassBranch.BOWMAN or (
                self.branch == ClassBranch.PIRATE and self in DEX_PIRATES):
            return Stat.DEX
        if self.branch == ClassBranch.THIEF:
            return Stat.LUK
        return Stat.STR

    @property
    def secondary_stat(self) -> Stat:
        if self.branch == ClassBranch.MAGICIAN:
            return Stat.LUK
        if self.branch == ClassBranch.BOWMAN or (
                self.branch == ClassBranch.PIRATE and self in DEX_PIRATES):
            return Stat.STR
        return Stat.DEX


CLASS_TO_BRANCH: Dict[CharClass, ClassBranch] = {
    CharClass.BEGINNER: ClassBranch.BEGINNER,
    CharClass.PATHFINDER: ClassBranch.BOWMAN,
    CharClass.BUCCANEER: ClassBranch.PIRATE,
    CharClass.KAISER: ClassBranch.WARRIOR,
}

STR_PIRATES: Set[CharClass] = {
    CharClass.SHADE,
    CharClass.BUCCANEER,
    CharClass.CANNON_MASTER,
    CharClass.THUNDER_BREAKER,
    CharClass.ARK,
}

DEX_PIRATES: Set[CharClass] = {
    CharClass.CORSAIR,
    CharClass.JETT,
    CharClass.ANGELIC_BUSTER,
}
