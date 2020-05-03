from enum import Enum, auto
from typing import Any, Dict, Set


class MapleStatsEnum(Enum):
    """Base enum class for the MapleStats project."""

    @classmethod
    def maybe_parse(cls, name: Any):
        if isinstance(name, cls):
            return name
        return cls[name.upper()]

    def to_json(self) -> str:
        return self.name


class World(MapleStatsEnum):
    """Enum representing all worlds."""
    BERA = auto()
    SCANIA = auto()
    AURORA = auto()
    ELYSIUM = auto()
    LUNA = auto()
    REBOOT = auto()
    REBOOT_EU = auto()

    @property
    def is_reboot(self):
        return "REBOOT" in self.name


class Stat(MapleStatsEnum):
    """Enum representing all types of stats."""
    ALL = auto()
    STR = auto()
    DEX = auto()
    INT = auto()
    LUK = auto()
    ATT = auto()
    MATT = auto()
    DMG = auto()
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
    BUFF_DURATION = auto()
    STATUS_RESIST = auto()
    STANCE = auto()
    BONUS_EXP = auto()
    DROP_RATE = auto()
    EQUIP_DROP_RATE = auto()
    IGNORE_ELEMENTAL_RESIST = auto()
    SCROLL_SUCCESS_RATE = auto()
    MONSTER_COLLECTION_ADD_CHANCE = auto()

    @property
    def default(self) -> Any:
        if self in FLOAT_VALUED_STATS:
            return 0.0
        return 0


FLOAT_VALUED_STATS: Set[Stat] = {
    Stat.IED,
    Stat.CRIT_DMG,
    Stat.BONUS_EXP,
    Stat.IGNORE_ELEMENTAL_RESIST,
    Stat.SCROLL_SUCCESS_RATE
}


class JobBranch(MapleStatsEnum):
    """Enum representing the five class branches."""
    BEGINNER = auto()
    WARRIOR = auto()
    MAGICIAN = auto()
    BOWMAN = auto()
    THIEF = auto()
    PIRATE = auto()


class Class(MapleStatsEnum):
    """Enum representing character classes."""
    BEGINNER = auto()
    ARAN = auto()
    EVAN = auto()
    MERCEDES = auto()
    PHANTOM = auto()
    SHADE = auto()
    LUMINOUS = auto()
    IL_ARCHMAGE = auto()
    FP_ARCHMAGE = auto()
    BISHOP = auto()
    BOWMASTER = auto()
    MARKSMAN = auto()
    PATHFINDER = auto()
    NIGHT_LORD = auto()
    SHADOWER = auto()
    DUAL_BLADE = auto()
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
    def branch(self) -> JobBranch:
        """Returns the branch of this class."""
        return CLASS_TO_BRANCH[self]

    @property
    def main_stat(self) -> Stat:
        if self.branch == JobBranch.MAGICIAN:
            return Stat.INT
        if self.branch == JobBranch.BOWMAN or (
                self.branch == JobBranch.PIRATE and self in DEX_PIRATES):
            return Stat.DEX
        if self.branch == JobBranch.THIEF:
            return Stat.LUK
        return Stat.STR

    @property
    def secondary_stat(self) -> Stat:
        if self.branch == JobBranch.MAGICIAN:
            return Stat.LUK
        if self.branch == JobBranch.BOWMAN or (
                self.branch == JobBranch.PIRATE and self in DEX_PIRATES):
            return Stat.STR
        return Stat.DEX


CLASS_TO_BRANCH: Dict[Class, JobBranch] = {
    Class.BEGINNER: JobBranch.BEGINNER,
    Class.PATHFINDER: JobBranch.BOWMAN,
    Class.BUCCANEER: JobBranch.PIRATE,
    Class.KAISER: JobBranch.WARRIOR,
}

STR_PIRATES: Set[Class] = {
    Class.SHADE,
    Class.BUCCANEER,
    Class.CANNON_MASTER,
    Class.THUNDER_BREAKER,
    Class.ARK,
}

DEX_PIRATES: Set[Class] = {
    Class.CORSAIR,
    Class.JETT,
    Class.ANGELIC_BUSTER,
}


class EquipType(MapleStatsEnum):
    """Enum representing equipment types that can give stats.

    RING_1 is the default ring equip slot.
    """
    WEAPON = auto()
    SECONDARY = auto()
    EMBLEM = auto()
    HAT = auto()
    TOP = auto()
    BOTTOM = auto()
    SHOE = auto()
    GLOVE = auto()
    CAPE = auto()
    SHOULDER = auto()
    RING_1 = auto()
    RING_2 = auto()
    RING_3 = auto()
    RING_4 = auto()
    PENDANT_1 = auto()
    PENDANT_2 = auto()
    BELT = auto()
    EARRING = auto()
    FACE = auto()
    EYE = auto()
    POCKET = auto()
    BADGE = auto()
    MEDAL = auto()
    ANDROID = auto()
    HEART = auto()
    TOTEM_1 = auto()
    TOTEM_2 = auto()
    TOTEM_3 = auto()
    PET_EQUIP_1 = auto()
    PET_EQUIP_2 = auto()
    PET_EQUIP_3 = auto()
    CASH_RING_1 = auto()
    CASH_RING_2 = auto()
    CASH_RING_3 = auto()
    CASH_RING_4 = auto()
    CASH_PENDANT = auto()


EMPTY_INVENTORY: Dict[EquipType, Any] = {
    equip_type: None for equip_type in EquipType}

WSE: Set[EquipType] = {
    EquipType.WEAPON,
    EquipType.SECONDARY,
    EquipType.EMBLEM
}


class WeaponType(MapleStatsEnum):

    SWORD_2H = auto()
    DAGGER = auto()
    KNUCKLE = auto()
    ANCIENT_BOW = auto()
    TUNER = auto()
