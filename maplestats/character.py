from enum import Enum
import json
from typing import Dict, Union

from maplestats.enums import ClassBranch, CharClass


JOB_ADVANCEMENT_LEVEL_REQUIREMENTS = [10, 30, 60, 100, 200]


class Character:

    def __init__(
        self,
        name: str,
        level: int,
        char_class: Union[CharClass, str],
        *args,
        **kwargs,
    ):
        del args
        del kwargs
        assert 1 <= level <= 275, 'Level must be between 1 and 275'

        self.name = name
        self.level = level
        self.char_class: CharClass = CharClass.maybe_parse(char_class)

    @property
    def job(self) -> int:
        """Job of this character"""
        for idx, lvl_req in enumerate(JOB_ADVANCEMENT_LEVEL_REQUIREMENTS):
            if self.level < lvl_req:
                return idx + 1
        return 5

    @property
    def class_branch(self) -> ClassBranch:
        return self.char_class.branch

    @property
    def pure_stat(self) -> int:
        """Pure stat from leveling up"""
        stat = 5 * self.level + 4
        if self.job >= 4:
            return stat + 10
        if self.job == 3:
            return stat + 5
        return stat

    def to_json(self, full: bool = False) -> Dict:
        """Returns the JSON representation of this character.

        Args:
            full: If True, includes all information about this character. If
                False, returns a minimal representation of this character.
        """
        minimal_repr = {
            'name': self.name,
            'level': self.level,
            'char_class': self.char_class
        }
        if not full:
            return minimal_repr

        full_repr = {
            **minimal_repr,
            'job': self.job,
            'class_branch': self.class_branch,
            'pure_stat': self.pure_stat,
        }
        for k, v in full_repr.items():
            if isinstance(v, Enum):
                full_repr[k] = v.name

        return full_repr

    def write_json(self, file_path: str = None) -> None:
        file_path = file_path if file_path else f'{self.name}.json'

        with open(file_path, 'w') as f:
            json.dump(self.to_json(), f)

    @classmethod
    def from_file(cls, file_path: str) -> 'Character':
        with open(file_path, 'r') as f:
            json_repr = json.load(f)
        return cls(**json_repr)

