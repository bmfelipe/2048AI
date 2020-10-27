import numpy as np
import random
def launch():
    #we need to store data in a matrix
    table = np.zeros(4*4,dtype="int")
    # self.matrix = [[0]*4 for i in range(4)]

    #start the game with initial twos
    # row = random.randint(0,3) row position
    # col = random.randint(0,3) column position
    twos_pos = np.random.default_rng().choice(16, 2, replace=False)
    table[twos_pos] = 2
    # self.cells[[row][col]["frame"].configure(bg=colors.TILE_COLORS[2])]
    # self.cells[[row][col]["number"].configure(bg=colors.TILE_COLORS[2],fg=colors.TILE_COLORS)]
    table = table.reshape((4, 4))
    return table
