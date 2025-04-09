from dataclasses import dataclass
from Options import (Choice, OptionList, NamedRange, 
    StartInventoryPool,
    PerGameCommonOptions, DeathLinkMixin)

class Difficulty(Choice):
    """Normal: Most people should play on this.
    Madhouse: Good luck, and thanks for testing deaths. Kappa
    Easy: No. Do Normal."""
    display_name = "Difficulty to Play On"
    option_normal = 0
    option_madhouse = 1
    default = 0

class UnlockedTypewriters(OptionList):
    """Specify the exact name of typewriters from the warp buttons in-game, as a YAML array.
    """
    display_name = "Unlocked Typewriters"

class BonusStart(Choice):
    """Some players might want to start with a little help in the way of a few extra heal items and packs of ammo.
    This option IS affected by cross-scenario weapon randomization, if that option is set.

    False: Normal, don't start with extra heal items and packs of ammo.
    True: Start with those helper items."""
    display_name = "Bonus Start"
    option_false = 0
    option_true = 1
    default = 0

# making this mixin so we can keep actual game options separate from AP core options that we want enabled
# not sure why this isn't a mixin in core atm, anyways
@dataclass
class StartInventoryFromPoolMixin:
    start_inventory_from_pool: StartInventoryPool

@dataclass
class RE7Options(StartInventoryFromPoolMixin, DeathLinkMixin, PerGameCommonOptions):
    difficulty: Difficulty
    unlocked_typewriters: UnlockedTypewriters
    bonus_start: BonusStart
