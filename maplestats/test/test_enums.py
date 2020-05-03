from maplestats.enums import JobBranch, CLASS_TO_BRANCH, STR_PIRATES, DEX_PIRATES


def test_pirates_have_main_stat() -> None:
    pirates_with_main_stat = STR_PIRATES | DEX_PIRATES
    for char_class, branch in CLASS_TO_BRANCH.items():
        if branch == JobBranch.PIRATE:
            assert char_class in pirates_with_main_stat
