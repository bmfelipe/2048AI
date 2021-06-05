import helper

from helper import *
from random import randint
from interface import *
import random
import numpy as np
from pynput.keyboard import Key, Controller



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
    # print("Horizontal moves: ",str(hm))
    vm = find_vertical_moves(matrix)
    # print("Vertical moves: ",str(vm))
    if not hm and not vm:
        return False
    else:
        return True


class  Game(Frame):
    def __init__(self,game_size=4):
        Frame.__init__(self)
        self.game_size = game_size
        self.matrix = refresh(game_size)
        self.score = 0
        self.screens = Screens.INIT

        self.master.bind("<Up>",self.swipe_up)
        self.master.bind("<Down>",self.swipe_down)
        self.master.bind("<Left>",self.swipe_left)
        self.master.bind("<Right>",self.swipe_right)
        

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
        print("Prob: ",str(prob))
        if (prob >=90):
            new_tile = 4
            print("Prob 10%")
        else:
            new_tile = 2
            print("Prob 90%")


        row = random.randint(0,3)
        col = random.randint(0,3)
        while(self.matrix[row][col] != 0):
            # Check another available cell
            row = random.randint(0,3)
            col = random.randint(0,3)
        self.matrix[row][col] = new_tile
        print("New tile: ",new_tile)


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
        # print("Inside try_move...")
        moves_l = moves_left(self.matrix)
        # print("Moves left: ",str(moves_l))
        if not moves_l:
            self.screens = Screens.LOSE
            return False

        moved = False
        rotations = 0
        back_rotations = 0
        if moves == Moves.SWIPE_UP:
            self.swipe_up()
            moved = True
            # rotations = 2
            # back_rotations = 2
        elif moves == Moves.SWIPE_DOWN:
            self.swipe_down()
            moved = True
            # rotations = 0
            # back_rotations = 0
        elif moves == Moves.SWIPE_LEFT:
            self.swipe_left()
            moved = True
            # rotations = 3
            # back_rotations = 1
        elif moves == Moves.SWIPE_RIGHT:
            self.swipe_right()
            moved = True
            # rotations = 1
            # back_rotations = 3
        else:
            return moved

        # helper.rotate_clockwise(self.matrix, rotations)

        # Merge then shift through empty space
        # merged = self.merge_down(self.matrix)
        # shifted = self.shift_down(self.matrix)
        # moved = merged or shifted

        # helper.rotate_clockwise(self.matrix, back_rotations)

        # if moved:
        #     self.show_random_tile()

        return moved

    
    def swipe_up(self):
        self.transpose()
        self.stack_cells()
        self.sum_cells()
        self.stack_cells()
        self.transpose()
        self.show_random_tile()
        # interf.refresh_screen()
        # self.is_over()


    
    def swipe_down(self):
        self.transpose()
        self.reverse()
        self.stack_cells()
        self.sum_cells()
        self.stack_cells()
        self.reverse()
        self.transpose()
        self.show_random_tile()
        # self.refresh_screen()
        # self.is_over()


    
    def swipe_left(self):
        self.stack_cells()
        self.sum_cells()
        self.stack_cells()
        self.show_random_tile()
        # self.refresh_screen()
        # self.is_over()

    def swipe_right(self):
        self.reverse()
        self.stack_cells()
        self.sum_cells()
        self.stack_cells()
        self.reverse()
        self.show_random_tile()
        # self.refresh_screen()
        # self.is_over()
 
 
    def stack_cells(self):
        stack_matrix = [[0] * 4 for _ in range(4)]
        for row_cnt in range(4):
            fill_pos = 0
            for col_cnt in range(4):
                if self.matrix[row_cnt][col_cnt] != 0:
                    stack_matrix[row_cnt][fill_pos] = self.matrix[row_cnt][col_cnt]
                    fill_pos += 1

        self.matrix = stack_matrix
        # print("Stacked matrix:")
        # print(self.matrix)
    
    def sum_cells(self):
        for row in range(4):
            for col in range(3):
                if self.matrix[row][col] != 0 and self.matrix[row][col] == self.matrix[row][col+1]:
                    self.matrix[row][col] *= 2
                    self.matrix[row][col+1] = 0
                    self.score += self.matrix[row][col]
        # print("Summed matrix:")
        # print(self.matrix)



    def reverse(self):
        reverse_matrix = [[0] * 4 for _ in range(4)]
        for row in range(4):
            for col in range(4):
                reverse_matrix[row][col] = self.matrix[row][3-col]
        self.matrix = reverse_matrix
    
    def transpose(self):
        self.matrix = np.asarray(self.matrix).transpose()
        # print("Transpose matrix")
        # print(self.matrix)



    





    


