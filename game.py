import tkinter as tk #GUI
import colors as colors 
import random
import numpy as np 

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.main_grid = tk.Frame(
            self, bg = colors.GRID_COLOR, bd=3, width=600, height=600
        )
        self.main_grid.grid(pady=(100,0))
        self.myGUI()
        self.launch()



        self.mainloop()

    def myGUI(self):
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
        # row = random.randint(0,3) row position
        # col = random.randint(0,3) column position
        # self.matrix[row,col] = 2
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




Game()