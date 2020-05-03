from collections import defaultdict
from typing import Any, Dict, Iterator, List, String, Union

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


def jsonify(data: Union[Dict, List, String]) -> Union[Dict, List, String]:
    """Converts data to JSON by calling `to_json()` for all nested objects which
    have this attribute.
    """

    def _handle_value(val: Any) -> Any:
        if isinstance(val, Dict):
            for k, v in val.items():
                val[k] = _handle_value(v)
            return val
        elif isinstance(val, List):
            return [_handle_value(k) for k in val]

        return val.to_json() if hasattr(val, "to_json") else val

    return _handle_value(data)


def parse_json(
        data: Dict, key_class: Any = None, value_class: Any = None) -> Dict:
    """Parse some jsonified data."""
    if key_class:
        assert hasattr(key_class, "maybe_parse")

    def _parse_key(k: Any) -> Any:
        return key_class.maybe_parse(k) if key_class else k

    def _parse_value(v: Any) -> Any:
        if not v:
            return v
        return value_class(**v) if value_class else v

    return {_parse_key(key): _parse_value(value) for key, value in data.items()}
