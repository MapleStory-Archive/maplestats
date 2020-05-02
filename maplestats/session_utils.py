import os
from typing import Optional

from maplestats.character import Character, LAST_MODIFIED_FILE_NAME


def load_last_modified() -> Optional[Character]:
    if not os.path.isfile(LAST_MODIFIED_FILE_NAME):
        return None

    with open(LAST_MODIFIED_FILE_NAME, 'r') as f:
        json_file = f.read()

    return Character.from_file(json_file) if os.path.isfile(json_file) else None
