from typing import Any, Dict, List, Tuple, Union

from maplestats.enums import Stat, EquipType
from maplestats.utils import STATS_TYPING, combine_stats, jsonify


class Equip:

    def __init__(
            self,
            name: str,
            equip_type: Union[EquipType, str],
            base_stats: STATS_TYPING = None,
            scroll_stats: STATS_TYPING = None,
            potential: List[Tuple[Stat, Any]] = None,
            bonus_potential: List[Tuple[Stat, Any]] = None,
            bonus_stats: List[Tuple[Stat, Any]] = None,
    ):
        """Note: Stats from star force counts as scroll stats."""
        self.name = name
        self._equip_type = equip_type
        self._base_stats = base_stats if base_stats else {}
        self._scroll_stats = scroll_stats if scroll_stats else {}
        self._potential = potential if potential else []
        self._bonus_potential = bonus_potential if bonus_potential else []
        self._bonus_stats = bonus_stats if bonus_stats else []

        assert len(self._potential) <= 3, (
            'Equip can only have up to 3 lines of potential')
        assert len(self._bonus_potential) <= 3, (
            'Equip can only have up to 3 lines of bonus potential')
        assert len(self._bonus_stats) <= 4, (
            'Equip can only have up to 4 lines of bonus stats')

        self._stats = self._get_stats()

    @property
    def equip_type(self) -> EquipType:
        return self._equip_type

    def _get_stats(self) -> STATS_TYPING:
        all_lines = self._potential + self._bonus_potential + self._bonus_stats
        return combine_stats([self._base_stats, self._scroll_stats] + [
            {stat: value} for stat, value in all_lines])

    @property
    def stats(self) -> STATS_TYPING:
        return self._stats

    def to_json(self) -> Dict[str, Any]:
        return jsonify({
            'name': self.name,
            'equip_type': self._equip_type,
            'base_stats': self._base_stats,
            'potential': self._potential,
            'bonus_potential': self._bonus_potential,
            'bonus_stats': self._bonus_stats,
        })
