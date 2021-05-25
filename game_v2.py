import helper

from helper import *
from random import randint
import random


def refresh(size):
    return [[0 for i in range(0, size)] for j in range(0, size)]

def find_horizontal_moves(matrix):
    for row in range(4):
        for col in range(3):
            if matrix[row][col] == matrix[row][col+1]:
                return True
    return False

def find_vertical_moves(matrix):
    for row in range(3):
        for col in range(4):
            if matrix[row][col] == matrix[row+1][col]:
                return True
    return False

def moves_left(matrix):
    hm = find_horizontal_moves(matrix)
    vm = find_vertical_moves(matrix)
    if not hm and not vm:
        return False
    else:
        return True


class Game:
    def __init__(self,game_size=4):
        self.game_size = game_size
        self.matrix = refresh(game_size)
        self.score = 0
        self.screens = Screens.INIT

    #getters
    def getScore(self):
        return self.score

    def getMatrix(self):
        return self.matrix

    def getGameSize(self):
        return self.game_size

    def getScreen(self):
        return self.screens

    def refresh_game(self,game_size=None):
        self.game_size = game_size if game_size is not None else self.game_size
        self.score = 0
        self.matrix = refresh(self.game_size)
        self.screens = Screens.IDLE
        self.show_random_tile()
        self.show_random_tile()

    def show_random_tile(self):
        prob = randint(1, 100)
        if prob >=90 :
            new_tile = 4
        else:
            new_tile = 2

        row = random.randint(0,3)
        col = random.randint(0,3)
        while(self.matrix[row][col] != 0):
            # Check another available cell
            row = random.randint(0,3)
            col = random.randint(0,3)
        self.matrix[row][col] = new_tile

    def count_cell_value(mat, val):
        cnt = 0
        for i in mat:
            for j in i:
                if j == val:
                    cnt = cnt +1
                
        return cnt

    def merge_down(self,matrix):
        merged = False
        for row in range(len(matrix) - 1, 0, -1):
            for col in range(0, len(matrix[row])):
                if matrix[row][col] != 0:
                    if matrix[row][col] == matrix[row - 1][col]:
                        merged = True
                        new_value = matrix[row][col] + matrix[row - 1][col]
                        matrix[row][col] = new_value
                        matrix[row - 1][col] = 0
                        self.score = self.score + new_value
        return merged

    def shift_down(self, matrix):
        shifted = False
        for row in range(len(matrix) - 1, -1, -1):
            for col in range(0, len(matrix[row])):
                temp_row = row
                while temp_row != len(matrix) - 1 and matrix[temp_row + 1][col] == 0:
                    shifted = True
                    matrix[temp_row + 1][col] = matrix[temp_row][col]
                    matrix[temp_row][col] = 0
                    temp_row = temp_row + 1

        return shifted

    def try_move(self,moves):
        moves_l = moves_left(self.matrix)
        if not moves_l:
            self.screens = Screens.LOSE
            return False

        moved = False
        rotations = 0
        back_rotations = 0
        if moves == Moves.SWIPE_UP:
            rotations = 2
            back_rotations = 2
        elif moves == Moves.SWIPE_DOWN:
            rotations = 0
            back_rotations = 0
        elif moves == Moves.SWIPE_LEFT:
            rotations = 3
            back_rotations = 1
        elif moves == Moves.SWIPE_RIGHT:
            rotations = 1
            back_rotations = 3
        else:
            return moved

        helper.rotate_clockwise(self.matrix, rotations)

        # Merge then shift through empty space
        merged = self.merge_down(self.matrix)
        shifted = self.shift_down(self.matrix)
        moved = merged or shifted

        helper.rotate_clockwise(self.matrix, back_rotations)

        if moved:
            self.show_random_tile()

        return moved

    





    


