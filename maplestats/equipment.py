from typing import Any, List, Tuple, Union

from maplestats.enums import Stat, EquipType
from maplestats.utils import STATS_TYPING, combine_stats


class Equip:

    def __init__(
            self,
            name: str,
            equip_type: Union[EquipType, str],
            base_stats: STATS_TYPING = None,
            potential: List[Tuple[Stat, Any]] = None,
            bonus_potential: List[Tuple[Stat, Any]] = None,
            bonus_stats: List[Tuple[Stat, Any]] = None,
    ):
        self.name = name
        self._equip_type = equip_type
        self._base_stats = base_stats if base_stats else {}
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

    def _get_stats(self) -> STATS_TYPING:
        all_lines = self._potential + self._bonus_potential + self._bonus_stats
        return combine_stats([self._base_stats] + [
            {stat: value} for stat, value in all_lines])

    @property
    def stats(self) -> STATS_TYPING:
        return self._stats
