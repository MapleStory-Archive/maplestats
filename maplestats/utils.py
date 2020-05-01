from collections import defaultdict
from typing import Any, Dict, Iterator

from maplestats.enums import Stat


STATS_TYPING = Dict[Stat, Any]


def combine_stats(stats_iter: Iterator[STATS_TYPING]) -> STATS_TYPING:
    """Combine multiple sources of stats into a single source."""

    def _combine_ied(ied_1: float, ied_2: float) -> float:
        """Combine two sources of IED into a single source."""
        return 1.0 - (1.0 - ied_1) * (1.0 - ied_2)

    combined_stats = defaultdict(lambda s: s.default)
    for stats in stats_iter:
        for stat, value in stats.items():
            if stat == Stat.IED:
                combined_stats[stat] = _combine_ied(combined_stats[stat], value)
            else:
                combined_stats[stat] += value

    return combined_stats
