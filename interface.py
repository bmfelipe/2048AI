from tkinter import *
import colors as colors 
from helper import Moves

# ------------------------------TRASH------------------------------


# FONT = ("Verdana", 40, "bold")


# class GameInterface(Frame):
#     def __init__(self,game):
#         self.game = game
#         self.matrix = game.getMatrix()

#         self.score = game.getScore()
#         self.matrix_size = len(self.matrix)

#         Frame.__init__(self)
#         self.grid()
#         self.master.title("2048")
#         self.main_grid = Frame(
#             self, bg = colors.GRID_COLOR, bd=3, width=600, height=600
#         )
#         self.main_grid.grid(pady=(100,0))

#         # self.matrix_positions = []
#         self.score_position = []
#         self.direction_grid_cells = []
#         # self.show_game()
#         # self.show_score()

#     def set_game(self,game):
#         self.game = game


#     def refresh_screen(self):
#         for row in range(4):
#             for col in range(4):
#                 cell_value = self.matrix[row][col]
#                 if cell_value == 0:
#                     self.cells[row][col]["frame"].config(bg=colors.EMPTY_CELL_COLOR)
#                     self.cells[row][col]["number"].config(bg=colors.EMPTY_CELL_COLOR, text="")
#                 else:                    
#                     # cell_number = Label(self.main_grid,bg=colors.EMPTY_CELL_COLOR)
#                     self.cells[row][col]["frame"].config(bg=colors.TILE_COLORS[cell_value])
#                     self.cells[row][col]["number"].config(
#                         bg=colors.TILE_COLORS[cell_value],
#                         fg=colors.NUMBERS_COLORS[cell_value],
#                         font=colors.LABEL_FONT,
#                         text=str(cell_value)
#                         )
#                 # self.cells.append(row)

#         self.score = self.game.getScore()
#         self.score_position[0].config(text="Score1: " + str(self.score))
#         self.update_idletasks()
#         # self.update()

#     def show_game(self):
#         self.cells = []
#         for i in range(4):
#             row = []
#             for j in range(4):
#                 cell_frame = Frame(
#                     self.main_grid,
#                     bg=colors.EMPTY_CELL_COLOR,
#                     width=150,
#                     height=150
#                 )
#                 cell_frame.grid(row=i,column=j, padx=7, pady=7)
#                 cell_number = Label(self.main_grid,bg=colors.EMPTY_CELL_COLOR)
#                 cell_number.grid(row=i,column=j)
#                 data = {
#                     "frame":cell_frame,
#                     "number":cell_number
#                 }
#                 row.append(data)
#             self.cells.append(row)

#         # score_f = Frame(self)
#         # score_f.place(relx=0.5, y=45, anchor="center")
#         # Label(score_f, text="fasdfa", font=colors.SCORE_LABEL_FONT).grid(row=0)
#         # self.score_l = Label(score_f, text="0", font=colors.SCORE_LABEL_FONT)
#         # self.score_l.grid(row=1)

#     def show_score(self):
#         score_f = Frame(self, width=50, height=50)
#         score_f.grid()
#         score_f.place(relx=0.5, y=45, anchor="center")

#         score_l = Label(master=score_f, text="Score2: " + str(self.score), justify=CENTER,font=colors.SCORE_LABEL_FONT)
#         self.score_position.append(score_l)
#         score_l.grid()
        
#         self.update()

#     def show_move(self):
#         direction_f = Frame(self, width=200, height=200)
#         direction_f.grid()
#         directions = [Moves.SWIPE_UP, Moves.SWIPE_LEFT, Moves.SWIPE_DOWN, Moves.SWIPE_RIGHT]
#         arrows = []
#         colors = ["#111111", "#222222", "#333333", "#444444"]
#         i = 0
#         for direction in directions:
#             arrow = Frame(direction_f, width=50, height=50)
#             text = Label(master=arrow, text=direction, bg=colors[i], font=("Verdana", 10, "bold"))
#             text.grid()
#             arrows.append(text)
#             i = i + 1
#         self.update()



        

