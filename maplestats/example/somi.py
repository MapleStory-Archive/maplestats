from maplestats.character import Character
from maplestats.enums import World, Class, EquipType
from maplestats.equipment import Equip

somi = Character(
    name='Somi',
    level=235,
    character_class=Class.BUCCANEER,
    world=World.ELYSIUM
)

somi.link_skills = {
    Class.FP_ARCHMAGE: 6,
    Class.NIGHT_LORD: 6,
    Class.BUCCANEER: 6,
    Class.BEAST_TAMER: 2,
    Class.WILD_HUNTER: 8,
    Class.DEMON_SLAYER: 2,
    Class.DEMON_AVENGER: 2,
    Class.ANGELIC_BUSTER: 2,
    Class.ARK: 2,
    Class.CADENA: 2,
    Class.KINESIS: 2,
    Class.KANNA: 2,
}

somi.equip(Equip(
    name='Arcane Umbra Knuckle',
    equip_type=EquipType.WEAPON,
    base_stats={},
    scroll_stats={},
    potential=[],
    bonus_potential=[],
    bonus_stats=[],
))

