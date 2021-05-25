import helper
from tkinter import *
import colors as colors 
from helper import Moves


FONT = ("Verdana", 40, "bold")

class GameInterface(Frame):
    def __init__(self,game):
        self.game = game
        self.score = game.getScore()
        self.matrix = game.getMatrix()
        self.matrix_size = len(self.matrix)
        Frame.__init__(self)
        self.matrix_positions = []
        self.score_position = []
        self.master.title("2048")
        self.show_game()
        self.show_score()

    def set_game(self,game):
        self.game = game

    def refresh_screen(self):
        self.matrix = self.game.getMatrix()
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                tmp = self.matrix[i][j]
                if tmp == 0:
                    self.matrix_positions[i][j].configure(text="", bg=colors.EMPTY_CELL_COLOR)
                else:
                    self.matrix_positions[i][j].configure(bg=colors.TILE_COLORS[tmp],fg=colors.NUMBERS_COLORS[tmp],font=colors.LABEL_FONT,text=str(tmp))

        self.score = self.game.getScore()
        self.score_position[0].config(text="Score: " + str(self.score))
        self.update_idletasks()
        self.update()

    def show_game(self):
        background = Frame(self,bg=colors.BACKGROUND_COLOR, width=1000 , height=1000)
        background.grid()
        matrix_frame = Frame(self,bg=colors.BACKGROUND_COLOR, width=600 , height=600)
        matrix_frame.grid()
        
        for i in range(self.matrix_size):
            rows = []

            for j in range(self.matrix_size):
                cell = Frame(matrix_frame, bg=colors.EMPTY_CELL_COLOR, width=500 / self.matrix_size,height=500 / self.matrix_size)
                cell.grid(row=i, column=j, padx=5, pady=5)
                c_aux = Label(master=cell, text="", bg=colors.EMPTY_CELL_COLOR, justify=CENTER, font=FONT, width=4,height=2)
                c_aux.grid()
                rows.append(c_aux)

            self.matrix_positions.append(rows)

        # matrix_frame.pack()
        

    def show_score(self):
        score_f = Frame(self, width=50, height=50)
        score_f.grid()
        score_f.place(relx=0.5, y=45, anchor="center")

        score_l = Label(master=score_f, text="Score: " + str(self.score), justify=CENTER,font=colors.SCORE_LABEL_FONT)
        self.score_position.append(score_l)
        score_l.grid()
        
        self.update()

    def show_move(self):
        direction_f = Frame(self, width=200, height=200)
        direction_f.grid()
        directions = [Moves.UP, Moves.LEFT, Moves.DOWN, Moves.RIGHT]
        arrows = []
        colors = ["#111111", "#222222", "#333333", "#444444"]
        i = 0
        for direction in directions:
            arrow = Frame(direction_f, width=50, height=50)
            text = Label(master=arrow, text=direction, bg=colors[i], font=("Verdana", 10, "bold"))
            text.grid()
            arrows.append(text)
            i = i + 1
        self.update()



        

