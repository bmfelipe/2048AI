import tkinter as tk #GUI
import colors as colors 

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
    


Game()