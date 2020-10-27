import tkinter as tk #GUI
import colors as colors 

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.mainloop()


gamegrid = Game()