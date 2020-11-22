import tkinter as tk #GUI
import colors as colors 
import random
import numpy as np


flag_over=0

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.main_grid = tk.Frame(
            self, bg = colors.GRID_COLOR, bd=3, width=600, height=600
        )
        self.main_grid.grid(pady=(100,0))
        self.interface()
        self.launch()

        self.master.bind("<Up>",self.swipe_up)
        self.master.bind("<Down>",self.swipe_down)
        self.master.bind("<Left>",self.swipe_left)
        self.master.bind("<Right>",self.swipe_right)


        self.mainloop()

    def interface(self):
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=colors.EMPTY_CELL_COLOR,
                    width=150,
                    height=150
                )
                cell_frame.grid(row=i,column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid,bg=colors.EMPTY_CELL_COLOR)
                cell_number.grid(row=i,column=j)
                data = {
                    "frame":cell_frame,
                    "number":cell_number
                }
                row.append(data)
            self.cells.append(row)

        score_f = tk.Frame(self)
        score_f.place(relx=0.5, y=45, anchor="center")
        tk.Label(score_f, text="Score", font=colors.SCORE_LABEL_FONT).grid(row=0)
        self.score_l = tk.Label(score_f, text="0", font=colors.SCORE_LABEL_FONT)
        self.score_l.grid(row=1)

    
    def launch(self):
        #we need to store data in a matrix
        self.matrix = np.zeros((4*4), dtype="int")
        twos_pos = np.random.default_rng().choice(16, 2, replace=False)
        self.matrix[twos_pos] = 2
        self.matrix = self.matrix.reshape((4,4))
 

        #start the game with initial twos

        result = np.where(self.matrix == 2)
        row = int(result[0][0])
        col = int(result[1][0])
        self.cells[row][col]["frame"].configure(bg=colors.TILE_COLORS[2])
        self.cells[row][col]["number"].configure(bg=colors.TILE_COLORS[2],fg=colors.NUMBERS_COLORS[2],font=colors.LABEL_FONT,text="2")

        row = int(result[0][1])
        col = int(result[1][1])
        self.cells[row][col]["frame"].configure(bg=colors.TILE_COLORS[2])
        self.cells[row][col]["number"].configure(bg=colors.TILE_COLORS[2],fg=colors.NUMBERS_COLORS[2],font=colors.LABEL_FONT,text="2")


        self.score=0


    def stack_cells(self):
        # stack_matrix = np.zeros((4*4),dtype="int")
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
                    # print("Score: "+str(self.score))
                    # print("matrix vaslue: "+str(self.matrix[row][col]))


    def reverse(self):
        reverse_matrix = [[0] * 4 for _ in range(4)]
        for row in range(4):
            # reverse_matrix.append([])
            for col in range(4):
                reverse_matrix[row][col] = self.matrix[row][3-col]
                # reverse_matrix[row].append(self.matrix[row][3-col])
        self.matrix = reverse_matrix
        # self.matrix = self.matrix[::-1]
    
    def transpose(self):
        # transpose_matrix = np.zeros((4*4),dtype="int")
        # for row in range(4):
        #     for col in range(4):
        #         transpose_matrix[row][col] = self.matrix[col][row]
        # self.matrix = transpose_matrix
        self.matrix = np.asarray(self.matrix).transpose()

    def show_random_tile(self):
        row = random.randint(0,3)
        col = random.randint(0,3)
        while(self.matrix[row][col] != 0):
            # Check another available cell
            row = random.randint(0,3)
            col = random.randint(0,3)
        self.matrix[row][col] = random.choice([2,4])

    def update_interface(self):
        for row in range(4):
            for col in range(4):
                cell_value = self.matrix[row][col]
                if cell_value == 0:
                    self.cells[row][col]["frame"].configure(bg=colors.EMPTY_CELL_COLOR)
                    self.cells[row][col]["number"].configure(bg=colors.EMPTY_CELL_COLOR, text="")
                else:
                    self.cells[row][col]["frame"].configure(bg=colors.TILE_COLORS[cell_value])
                    self.cells[row][col]["number"].configure(
                        bg=colors.TILE_COLORS[cell_value],
                        fg=colors.NUMBERS_COLORS[cell_value],
                        font=colors.LABEL_FONT,
                        text=str(cell_value)
                        )
        self.score_l.configure(text=self.score)
        self.update_idletasks()

    def swipe_up(self,event):
        self.transpose()
        self.stack_cells()
        self.sum_cells()
        self.stack_cells()
        self.transpose()
        self.show_random_tile()
        self.update_interface()
        self.is_over()


    
    def swipe_down(self,event):
        self.transpose()
        self.reverse()
        self.stack_cells()
        self.sum_cells()
        self.stack_cells()
        self.reverse()
        self.transpose()
        self.show_random_tile()
        self.update_interface()
        self.is_over()


    
    def swipe_left(self,event):
        self.stack_cells()
        self.sum_cells()
        self.stack_cells()
        self.show_random_tile()
        self.update_interface()
        self.is_over()

    def swipe_right(self,event):
        self.reverse()
        self.stack_cells()
        self.sum_cells()
        self.stack_cells()
        self.reverse()
        self.show_random_tile()
        self.update_interface()
        self.is_over()

    def find_horizontal_moves(self):
        for row in range(4):
            for col in range(3):
                if self.matrix[row][col] == self.matrix[row][col+1]:
                    return True
        return False

    def find_vertical_moves(self):
        for row in range(3):
            for col in range(4):
                if self.matrix[row][col] == self.matrix[row+1][col]:
                    return True
        return False

    def is_over(self):
        if any(2048 in row for row in self.matrix):
            is_over_frame =  tk.Frame(self.main_grid,borderwidth=2)
            is_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(is_over_frame, text="Victory", bg=colors.EMPTY_CELL_COLOR, fg=colors.NUMBERS_COLORS[2], font=colors.SCORE_LABEL_FONT).pack()
            flag_over=1
        elif not any(0 in row for row in self.matrix) and not self.find_horizontal_moves() and not self.find_vertical_moves():
            is_over_frame =  tk.Frame(self.main_grid,borderwidth=2)
            is_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(is_over_frame, text="Game Over", bg=colors.EMPTY_CELL_COLOR, fg=colors.NUMBERS_COLORS[2], font=colors.SCORE_LABEL_FONT).pack()
            flag_over=1


def main():
    Game()
    print(str(flag_over))

if __name__=='__main__':
    main()





          




