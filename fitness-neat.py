import game_v2
from game_v2 import *
import interface
from interface import *
import helper
import math
import neat
from math import log2


inputs = []

def redimension_input_matrix(arr):
    val = max(arr)
    log_val = log2(val)
    if log_val == 0:
        return
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i] = log2(arr[i]) / log_val

    return arr

for i in range(4):
    tmp = []
    [tmp.append(0) for j in range(4)]
    inputs.append(tmp)

outputs = [0,0,0,0]

game = Game(4)
interf = GameInterface(game)

def calc_smoothness(game):
    matrix = game.getMatrix()
    smoothness = 0
    # Only rotate twice to avoid double counting
    # Ignore 0 tiles
    for rotation in range(2):
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] != 0 and j + 1 < len(matrix[i]) and matrix[i][j + 1] != 0:
                    current_smoothness = math.fabs(log2(matrix[i][j]) - log2(matrix[i][j + 1]))
                    smoothness = smoothness - current_smoothness
        helper.rotate_clockwise(matrix)

    return smoothness

def fitness(game, timedOut=False):
    score = game.getScore()
    smoothness = calc_smoothness(game)
    matrix = [i for j in game.getMatrix() for i in j]

    return (score * score_w / (smoothness * smoothness_w)) * log2(max(board)) * -1


def map_movement(pos):
    if pos == 0:
        return Moves.SWIPE_UP
    elif pos == 1:
        return Moves.SWIPE_DOWN
    elif pos == 2:
        return Moves.SWIPE_LEFT
    elif pos == 3:
        return Moves.SWIPE_RIGHT

def genomes(genome_id, genome, config):
    genome.fitness = 0.0
    network = neat.nn.FeedForwardNetwork.create(genome, config)
    game.restart_game()
    interf.set_game(game)

    # Play game till game over, then evaluate fitness
    is_over = False
    matrix = game.getMatrix()
    consecutive_not_moved = 0
    ok_moves = 0
    while not is_over:
        entrada = redimension_input_matrix([j for i in matrix for j in i])
        salida = network.activate(inputs)
        output_moves = [(map_movement(i), salida[i]) for i in range(len(salida))]
        output_moves = sorted(output_moves, key=lambda x: x[1])

        for (direction, weight) in output_moves:
            moved = game.try_move(direction)
            if moved:
                break

        if moved:
            interf.refresh_screen()
            ok_moves = ok_moves + 1
        else:
            consecutive_not_moved = consecutive_not_moved + 1

        if game.getScreen() == Screens.WIN or game.getScreen() == Screens.LOSS:
            game_over = True
        elif consecutive_not_moved == 15:
            game_over = True

    genome.fitness = fitness(game, consecutive_not_moved == 15)


def all_genomes(genomes, config):
    for genome_id, genome in genomes:
        genomes(genome_id, genome, config)