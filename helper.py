from enum import Enum

class Keyz(Enum):
    UP = "W"
    DOWN = "S"
    RIGHT = "D"
    LEFT ="A"
    RESET = "R"
    ENTER = "Enter"

class Moves(Enum):
    SWIPE_UP = "up"
    SWIPE_DOWN = "down"
    SWIPE_RIGHT = "right"
    SWIPE_LEFT ="left"

class Screens(Enum):
    WIN = "win"
    LOSE = "lose"
    MOVING = "moving"
    IDLE = "idle"
    INIT = "init"

mapped_moves = {None: None, Keyz.UP: Moves.UP, Keyz.DOWN: Moves.DOWN, Keyz.LEFT: Moves.LEFT, Keyz.RIGHT: Moves.RIGHT}
mapped_keyz = {None: None, "w": Keyz.UP, "s": Keyz.DOWN, "a": Keyz.LEFT, "d": Keyz.RIGHT}

def key_to_move(key):
    return mapped_moves[key]


def char_to_key(char):
    return mapped_keyz[char]


def char_to_move(char):
    return mapped_moves[mapped_keyz[char]]
