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
        self.grid()
        self.master.title("2048")
        self.main_grid = Frame(
            self, bg = colors.GRID_COLOR, bd=3, width=600, height=600
        )
        self.main_grid.grid(pady=(100,0))



        self.game_size = game_size
        self.matrix = refresh(game_size)
        self.score = 0
        self.screens = Screens.INIT
        self.score_position = []


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

    def interface(self):
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = Frame(
                    self.main_grid,
                    bg=colors.EMPTY_CELL_COLOR,
                    width=150,
                    height=150
                )
                cell_frame.grid(row=i,column=j, padx=5, pady=5)
                cell_number = Label(self.main_grid,bg=colors.EMPTY_CELL_COLOR)
                cell_number.grid(row=i,column=j)
                data = {
                    "frame":cell_frame,
                    "number":cell_number
                }
                row.append(data)
            self.cells.append(row)
        score_f = Frame(self, width=50, height=50)
        score_f.grid()
        score_f.place(relx=0.5, y=45, anchor="center")

        score_l = Label(master=score_f, text="Score2: " + str(self.score), justify=CENTER,font=colors.SCORE_LABEL_FONT)
        self.score_position.append(score_l)
        score_l.grid()
        
        self.update()

    def refresh_screen(self):
        for row in range(4):
            for col in range(4):
                cell_value = self.matrix[row][col]
                if cell_value == 0:
                    self.cells[row][col]["frame"].config(bg=colors.EMPTY_CELL_COLOR)
                    self.cells[row][col]["number"].config(bg=colors.EMPTY_CELL_COLOR, text="")
                else:                    
                    # cell_number = Label(self.main_grid,bg=colors.EMPTY_CELL_COLOR)
                    self.cells[row][col]["frame"].config(bg=colors.TILE_COLORS[cell_value])
                    self.cells[row][col]["number"].config(
                        bg=colors.TILE_COLORS[cell_value],
                        fg=colors.NUMBERS_COLORS[cell_value],
                        font=colors.LABEL_FONT,
                        text=str(cell_value)
                        )
                # self.cells.append(row)

        self.score = self.getScore()
        self.score_position[0].config(text="Score1: " + str(self.score))
        self.update_idletasks()
        # self.update()


    def refresh_game(self,game_size=None):
        self.game_size = game_size if game_size is not None else self.game_size
        self.score = 0
        self.matrix = refresh(self.game_size)
        self.screens = Screens.IDLE
        self.show_random_tile()
        self.show_random_tile()

    
    def show_random_tile(self):
        prob = randint(1, 100)
        if (prob >=90):
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
        if moves == Moves.SWIPE_UP:
            self.swipe_up()
            moved = True
        elif moves == Moves.SWIPE_DOWN:
            self.swipe_down()
            moved = True
        elif moves == Moves.SWIPE_LEFT:
            self.swipe_left()
            moved = True
        elif moves == Moves.SWIPE_RIGHT:
            self.swipe_right()
            moved = True
        else:
            return moved

        return moved

    
    def swipe_up(self):
        self.transpose()
        self.stack_cells()
        self.sum_cells()
        self.stack_cells()
        self.transpose()
        self.show_random_tile()
        # self.refresh_screen()
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
    
    def sum_cells(self):
        for row in range(4):
            for col in range(3):
                if self.matrix[row][col] != 0 and self.matrix[row][col] == self.matrix[row][col+1]:
                    self.matrix[row][col] *= 2
                    self.matrix[row][col+1] = 0
                    self.score += self.matrix[row][col]


    def reverse(self):
        reverse_matrix = [[0] * 4 for _ in range(4)]
        for row in range(4):
            for col in range(4):
                reverse_matrix[row][col] = self.matrix[row][3-col]
        self.matrix = reverse_matrix
    
    def transpose(self):
        self.matrix = np.asarray(self.matrix).transpose()



    





    


