from enum import Enum
import numpy as np

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

mapped_moves = {None: None, Keyz.UP: Moves.SWIPE_UP, Keyz.DOWN: Moves.SWIPE_DOWN, Keyz.LEFT: Moves.SWIPE_LEFT, Keyz.RIGHT: Moves.SWIPE_RIGHT}
mapped_keyz = {None: None, "w": Keyz.UP, "s": Keyz.DOWN, "a": Keyz.LEFT, "d": Keyz.RIGHT}

def key_to_move(key):
    return mapped_moves[key]


def char_to_key(char):
    return mapped_keyz[char]


def char_to_move(char):
    return mapped_moves[mapped_keyz[char]]

def start():
    matrix = np.zeros((16), dtype="int")
    initial_twos = np.random.default_rng().choice(16, 2, replace=False)
    matrix[initial_twos] = 2
    matrix = matrix.reshape((4, 4))
    return matrix

# def rotate_clockwise(arr, iteration = 1):
#     if iteration <= 0:
#         return

#     l = len(arr)
#     for i in range(0, iteration):
#         for s in range(0, int(l / 2)):
#             for j in range(0, l - (2 * s) - 1):
#                 temp = arr[s][s + j]
#                 arr[s][s + j] = arr[l - s - j - 1][s]
#                 arr[l - s - j - 1][s] = arr[l - s - 1][l - s - j - 1]
#                 arr[l - s - 1][l - s - j - 1] = arr[s + j][l - s - 1]
#                 arr[s + j][l - s - 1] = temp

#     return arr
